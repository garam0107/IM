import sys
sys.stdin = open('input (2).txt','r')
def maze_2(N,arr1,start):
    r,c = start[0],start[1]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    stack=[(r,c)]
    arr1[r][c] = 1
    while stack:
        r,c = stack.pop()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr1[nr][nc] == 0:
                    stack.append((nr,nc))
                    arr1[nr][nc] = 1
                elif arr1[nr][nc] == 3:
                    return 1

    return 0




T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    maze_list = [list(map(int,input())) for _ in range(N)]
    start = []
    for i in range(N):
        for j in range(N):
            if maze_list[i][j] == 2:
                start.append(i)
                start.append(j)
                break
    answer = maze_2(N,maze_list,start)
    print(f'#{tc} {answer}')