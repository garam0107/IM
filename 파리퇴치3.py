def remove1(N,M,arr,i,j):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    sum = arr[i][j]
    for k in range(4):
        for add in range(1,M):
            nr = i + dr[k] * add
            nc = j + dc[k] * add
            if 0 <= nr < N and 0 <= nc < N:
                sum += arr[nr][nc]

    return sum
def remove2(N,M,arr,i,j):
    dr = [-1,1,1,-1]
    dc = [1,1,-1,-1]
    sum = arr[i][j]
    for k in range(4):
        for add in range(1,M):
            nr = i + dr[k] * add
            nc = j + dc[k] * add
            if 0 <= nr < N and 0 <= nc < N:
                sum += arr[nr][nc]
    return sum




T= int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    bug_arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            answer = max(remove1(N,M,bug_arr,i,j),remove2(N,M,bug_arr,i,j))
            if max_v < answer:
                max_v = answer
    print(f'#{tc} {max_v}')

