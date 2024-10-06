from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction_mapping = ['U', 'R', 'D', 'L']

def bfs(my_position, target_position, K):
    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    print(visited)
    q = deque()
    x, y = my_position
    q.append((x, y, 0, 0, K, []))
    visited[x][y][0][K] = True

    while q:
        x, y, dir, moves, cnt, path = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]

        if [nx, ny] == target_position:
            path.append((direction_mapping[dir], (nx, ny), 'F'))  # 목적지 도달 시 'F' 추가
            return path

        if 0 <= nx < N and 0 <= ny < N:
            if map_data[nx][ny] == 'G' and not visited[nx][ny][dir][cnt]:
                visited[nx][ny][dir][cnt] = True
                q.append((nx, ny, dir, moves + 1, cnt, path + [(direction_mapping[dir], (nx, ny), 'A')]))  # 'A' 추가
            #
            # elif map_data[nx][ny] == 'X' and cnt > 0 and not visited[nx][ny][dir][cnt - 1]:
            #     print(1)
            #     visited[nx][ny][dir][cnt - 1] = True
            #     q.append((nx, ny, dir, moves + 1, cnt - 1, path + [(direction_mapping[dir], (nx, ny), 'A')]))  # 'A' 추가
            # elif 0 <= nx < N and 0 <= ny < N:
            #     if map_data[nx][ny] == 'F'  and not visited[nx][ny][dir][cnt]:

        nd = (dir - 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = True
            q.append((x, y, nd, moves + 1, cnt, path))

        nd = (dir + 1) % 4
        if not visited[x][y][nd][cnt]:
            visited[x][y][nd][cnt] = True
            q.append((x, y, nd, moves + 1, cnt, path))

    return []

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    map_data = [list(input().split()) for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if map_data[x][y] == 'A':
                my_position = [x, y]
            elif map_data[x][y] == 'X':
                target_position = [x, y]

    path = bfs(my_position, target_position, K)

    print(f'#{tc} {len(path)}')
    print(path)
    for command, position, action in path:
        print(f'{command} {action} {position}')  # action에 따라 'A' 또는 'F' 출력



