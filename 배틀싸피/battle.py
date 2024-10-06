from libs._bridge import init, submit, close

NICKNAME = '기본코드'
game_data = init(NICKNAME)

# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보
allies = {}  # 아군 정보
enemies = {}  # 적군 정보
codes = []  # 주어진 암호문
directions = ['U', 'R', 'D', 'L']  # 방향: 위, 오른쪽, 아래, 왼쪽


# 암호 해독 함수
def decrypt_code(code):
    def decrypt_letter(letter):
        return chr(((ord(letter) - ord('A') - 7) % 26) + ord('A'))

    return ''.join(decrypt_letter(c) for c in code)


# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    game_data_rows = game_data.split('\n')
    row_index = 0
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])
    map_width = int(header[1])
    num_of_allies = int(header[2])
    num_of_enemies = int(header[3])
    num_of_codes = int(header[4])
    row_index += 1

    # 맵 정보 읽기
    global map_data
    map_data = [['' for c in range(map_width)] for r in range(map_height)]
    for i in range(map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    # 아군 정보 읽기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 적군 정보 읽기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 암호문 정보 읽기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])


# 경로 탐색 및 동작 결정
def decide_action():
    my_position = None
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':  # 내 위치를 찾음
                my_position = (i, j)
                break
        if my_position:
            break

    # 목표는 적 포탑으로 설정
    target_position = None
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'X':  # 적 포탑 위치 찾기
                target_position = (i, j)
                break
        if target_position:
            break

    # 포탄 확인 (일반 포탄 수 확인)
    normal_ammo = int(allies['A'][2])
    has_ammo = normal_ammo > 0

    # 경로 탐색: 모든 방향(상, 하, 좌, 우) 탐색 가능하게 수정
    next_step = None

    # 오른쪽으로 이동 가능하면 이동
    if my_position[1] < len(map_data[0]) - 1 and map_data[my_position[0]][my_position[1] + 1] == 'G':
        next_step = (my_position[0], my_position[1] + 1)  # 오른쪽으로 이동 가능
        direction = 'R A'  # 명령: 오른쪽 이동

    # 아래로 이동 가능하면 이동
    elif my_position[0] < len(map_data) - 1 and map_data[my_position[0] + 1][my_position[1]] == 'G':
        next_step = (my_position[0] + 1, my_position[1])  # 아래로 이동 가능
        direction = 'D A'  # 명령: 아래 이동

    # 위로 이동 가능하면 이동
    elif my_position[0] > 0 and map_data[my_position[0] - 1][my_position[1]] == 'G':
        next_step = (my_position[0] - 1, my_position[1])  # 위로 이동 가능
        direction = 'U A'  # 명령: 위 이동

    # 왼쪽으로 이동 가능하면 이동
    elif my_position[1] > 0 and map_data[my_position[0]][my_position[1] - 1] == 'G':
        next_step = (my_position[0], my_position[1] - 1)  # 왼쪽으로 이동 가능
        direction = 'L A'  # 명령: 왼쪽 이동

    # 보급시설(F)에 도착하면 포탄 획득
    if next_step and map_data[next_step[0]][next_step[1]] == 'F':
        if codes:
            decrypted_code = decrypt_code(codes.pop(0))
            print(f'보급시설 암호 해독: {decrypted_code}')
            allies['A'][2] = str(normal_ammo + 1)  # 일반 포탄 추가
            print(f'일반 포탄 획득! 현재 포탄 수: {allies["A"][2]}')
            return f'{direction} F'  # 보급시설에서 포탄을 획득하고 그 방향으로 명령 수행

    # 공격 결정 (적 포탑 또는 나무가 있으면 공격)
    if next_step and map_data[next_step[0]][next_step[1]] == 'X' and has_ammo:
        # 공격 성공 시 적 포탑 제거
        map_data[next_step[0]][next_step[1]] = 'G'  # 포탑을 제거하고 그 자리를 'G'로 만듦
        allies['A'][2] = str(normal_ammo - 1)  # 포탄 사용
        print(f'적 포탑 제거! 남은 포탄 수: {allies["A"][2]}')
        return f'{direction} F M'  # 오른쪽으로 일반 포탄 발사

    elif next_step and map_data[next_step[0]][next_step[1]] == 'T' and has_ammo:
        # 나무 제거
        map_data[next_step[0]][next_step[1]] = 'G'  # 나무를 제거하고 그 자리를 'G'로 만듦
        allies['A'][2] = str(normal_ammo - 1)  # 포탄 사용
        print(f'나무 제거! 남은 포탄 수: {allies["A"][2]}')
        return f'{direction} F M'  # 나무 파괴

    # 이동 불가한 타일(돌)을 처리: 돌을 만나면 그 자리에 멈추고 다른 경로를 탐색
    if next_step and map_data[next_step[0]][next_step[1]] == 'B':
        print("돌을 만났습니다. 이동할 수 없습니다.")
        return 'S'  # Stay 명령

    # 이미 결정된 방향에 따라 명령 반환 (위, 아래, 왼쪽, 오른쪽 이동 중 하나)
    if next_step:
        return direction  # 방향 이동

    return 'S'  # 이동할 수 없을 경우 유지 명령


# 메인 반복문: 배틀싸피 메인 프로그램과 데이터를 주고받는 부분
while game_data is not None:
    parse_data(game_data)

    # 동작 결정
    output = decide_action()

    # output을 submit 함수로 전달
    game_data = submit(output)

# 반복문을 빠져나오면 메인 프로그램과의 연결 해제
close()