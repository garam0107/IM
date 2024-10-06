dir_position = ['U','R','D','L']
dr = [-1,0,1,0]
dc = [0,1,0,-1]

from collections import  deque
def bfs(my_position, target_position):
    visited = [[[False] * 4 for _ in range(N)]for _ in range(N)]
    q = deque()
    x,y = my_position

    q.append((x,y,0,[]))
    visited[x][y][0] = True


    while True:
        x,y,dir,path = q.popleft()
        nr = x + dr[dir]
        nc = y + dc[dir]

        if [nr,nc] == target_position:
            path.append((dir_position[dir], 'F'))
            return path


        if 0 <= nr < N and 0 <= nc < N:
            if map_data[nr][nc] == 'G' and not visited[nr][nc][dir]:
                visited[nr][nc][dir] = True
                q.append((nr,nc,dir,path+[(dir_position[dir], 'A')]))


        nd = (dir-1) % 4
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x,y,nd,path))

        nd = (dir+1) % 4
        if not visited[x][y][nd]:
            visited[x][y][nd] = True
            q.append((x,y,nd,path))




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

    print(path)  # 경로 출력
    for command, action in path:
        print(f'{command} {action}')  # 각 이동에 대해 명령과 위치 출력