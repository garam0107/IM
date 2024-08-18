T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail_list = [[0]*N for _ in range(N)]
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    i = 0
    r = 0
    c = 0
    counts= 1
    snail_list[r][c] = counts
    while counts < N ** 2:
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if snail_list[nr][nc] ==0:
                counts += 1
                snail_list[nr][nc] = counts
                r = nr
                c = nc
            else:
                i = (i+1)%4
        else:
            i = (i+1)%4


    print(snail_list)



