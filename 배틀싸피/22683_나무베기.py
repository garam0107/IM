from collections import deque  # deque를 사용하기 위해 import

# 상하좌우 방향을 정의하는 리스트
dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌의 x좌표 변화량
dy = [0, 1, 0, -1]  # 상, 우, 하, 좌의 y좌표 변화량

# 0, 1, 2, 3
direction_mapping = ['U', 'R', 'D', 'L']  # 방향을 문자로 매핑

def bfs(my_position, target_position):
    # 방문 여부를 기록하기 위한 4차원 배열 생성
    visited = [[[False] * 4  for _ in range(N)] for _ in range(N)]
    q = deque()  # BFS에 사용할 큐 초기화
    x, y = my_position  # 내 현재 위치를 unpack
    q.append((x, y, 0,[]))  # 큐에 현재 위치, 방향, 이동 횟수, 남은 폭탄 횟수, 경로를 추가
    visited[x][y][0] = True  # 현재 위치를 방문했다고 표시

    # BFS 루프 시작
    while q:
        # 큐에서 현재 위치, 방향, 이동 횟수, 남은 폭탄 횟수, 경로를 가져옴
        x, y, dir, path = q.popleft()
        nx = x + dx[dir]  # 다음 x좌표 계산
        ny = y + dy[dir]  # 다음 y좌표 계산

        # 만약 다음 위치가 목표 위치라면
        if [nx, ny] == target_position:
            path.append((direction_mapping[dir], 'F'))  # 도달 시 'F' 추가
            return path  # 최종 경로 반환

        # 맵의 범위를 체크하고
        if 0 <= nx < N and 0 <= ny < N:
            # 다음 위치가 'G'인 경우 (이동 가능 구역)
            if map_data[nx][ny] == 'G' and not visited[nx][ny][dir]:
                visited[nx][ny][dir] = True  # 방문 기록
                # 다음 위치, 방향, 이동 횟수, 남은 폭탄 횟수, 경로 추가
                q.append((nx, ny, dir, path + [(direction_mapping[dir], 'A')]))  # 'A' 추가

            # 'X'인 경우 (폭탄을 사용해야 하는 구역)
            # elif map_data[nx][ny] == 'X' and cnt > 0 and not visited[nx][ny][dir][cnt - 1]:
            #     print(1)
            #     visited[nx][ny][dir][cnt - 1] = True  # 방문 기록
            #     q.append((nx, ny, dir, moves + 1, cnt - 1, path + [(direction_mapping[dir], (nx, ny), 'A')]))  # 'A' 추가

        # 방향을 바꾸는 경우: 왼쪽 회전
        nd = (dir - 1) % 4
        if not visited[x][y][nd]:  # 아직 방문하지 않았다면
            visited[x][y][nd] = True  # 방문 기록
            q.append((x, y, nd, path))  # 방향만 바꾸고 현재 위치에 추가

        # 방향을 바꾸는 경우: 오른쪽 회전
        nd = (dir + 1) % 4
        if not visited[x][y][nd]:  # 아직 방문하지 않았다면
            visited[x][y][nd] = True  # 방문 기록
            q.append((x, y, nd, path))  # 방향만 바꾸고 현재 위치에 추가

    return []  # 경로를 찾지 못한 경우 빈 리스트 반환

# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    # 맵의 크기(N)와 폭탄의 개수(K) 입력
    N= int(input())
    # 맵 데이터 입력
    map_data = [list(input().split()) for _ in range(N)]

    # 아군('A')와 목표('X')의 위치 찾기
    for x in range(N):
        for y in range(N):
            if map_data[x][y] == 'A':
                my_position = [x, y]  # 아군 위치 저장
            elif map_data[x][y] == 'X':
                target_position = [x, y]  # 목표 위치 저장

    # BFS를 호출하여 경로 찾기
    path = bfs(my_position, target_position)

    # 결과 출력
    print(f'#{tc} {len(path)}')  # 테스트 케이스 번호와 경로의 길이 출력
    print(path)  # 경로 출력
    for command, action in path:
        print(f'{command} {action}')  # 각 이동에 대해 명령과 위치 출력
# while game_data is not None:
#     parse_data(game_data)
#
#     my_position = [-1, -1]
#     for i in range(len(map_data)):
#         for j in range(len(map_data[0])):
#             if map_data[i][j] == 'A':
#                 my_position = [i, j]
#             elif map_data[i][j] == 'X':
#                 target_position = [i, j]
#
#
#     path = bfs(my_position, target_position, 1)
#
#
#     output = ''
#     if path:
#         for command, position, action in path:
#             output += f'{command} {action} '
#
#     if not output:
#         output = 'S'  # 알고리즘 결괏값이 없을 경우를 대비하여 초기값을 S로 설정
#
#     print(f'----출력----\n{output}\n--------------')
#     game_data = submit(output)


