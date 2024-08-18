def ladder_check(arr1,arr2):
    min_v = 10000
    N = 100
    dr = [0,0,1]
    dc = [1,-1,0]
    result = 0
    for start in arr2:
        visit = [[0]* N for _ in range(N)]
        r = 0
        c = start
        counts = 0
        while r < 99:
            for k in range(3):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and arr1[nr][nc]==1:
                    visit[nr][nc] = 1
                    r = nr
                    c = nc
                    counts += 1
        if min_v > counts:
            min_v = counts
            result = start

    return result


T = 10
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start_list = [i for i in range(100) if ladder[0][i] == 1]
    answer = ladder_check(ladder,start_list)
    print(f'#{tc} {answer}')



