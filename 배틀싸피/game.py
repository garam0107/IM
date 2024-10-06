from collections import deque
from libs._bridge import init, submit, close

NICKNAME = '기본코드'
game_data = init(NICKNAME)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction_mapping = ['U', 'R', 'D', 'L']

map_data = [[]]  # 맵 정보
allies = {}  # 아군 정보
enemies = {}  # 적군 정보
codes = []  # 주어진 암호문

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    global map_data, allies, enemies, codes
    game_data_rows = game_data.split('\n')
    row_index = 0

    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])
    map_width = int(header[1])
    num_of_allies = int(header[2])
    num_of_enemies = int(header[3])
    num_of_codes = int(header[4])
    row_index += 1

    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

def bfs(my_position, target_position, K):
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(len(map_data))] for _ in range(len(map_data[0]))]
    q = deque()
    x, y = my_position
    q.append((x, y, 0, 0, K, []))
    visited[x][y][0][K] = True

    while q:
        x, y, dir, moves, cnt, path = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]

        if [nx, ny] == target_position:
            path.append((direction_mapping[dir], (nx, ny), 'F'))
            return path

        if 0 <= nx < len(map_data) and 0 <= ny < len(map_data[0]):
            if map_data[nx][ny] == 'G' and not visited[nx][ny][dir][cnt]:
                visited[nx][ny][dir][cnt] = True
                q.append((nx, ny, dir, moves + 1, cnt, path + [(direction_mapping[dir], (nx, ny), 'A')]))  # 'A' 추가

            elif map_data[nx][ny] == 'X' and cnt > 0 and not visited[nx][ny][dir][cnt - 1]:
                visited[nx][ny][dir][cnt - 1] = True
                q.append((nx, ny, dir, moves + 1, cnt - 1, path + [(direction_mapping[dir], (nx, ny), 'A')]))  # 'A' 추가

        nd = (dir - 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = True
            q.append((x, y, nd, moves + 1, cnt, path))

        nd = (dir + 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = True
            q.append((x, y, nd, moves + 1, cnt, path))

    return []

# 메인 반복문
while game_data is not None:
    parse_data(game_data)

    my_position = [-1, -1]
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 'A':
                my_position = [i, j]
            elif map_data[i][j] == 'X':
                target_position = [i, j]


    path = bfs(my_position, target_position, 1)


    output = ''
    if path:
        for command, position, action in path:
            output += f'{command} {action} '

    if not output:
        output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정

    print(f'----출력----\n{output}\n--------------')
    game_data = submit(output)

close()
