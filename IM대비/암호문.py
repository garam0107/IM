T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    num = list(range(1,N^2+1))
    counts = 1
    row = 0
    col = 0
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    arr[row][col] = 1
    while counts < N ** 2:
        for idx in range(4):
            nr = row + dr[idx]
            nc = col + dc[idx]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    counts += 1
                    arr[nr][nc] = counts
                    row = nr
                    col = nc
                    break


    print(f'#{tc}')
    for i in arr:
        print(*i)