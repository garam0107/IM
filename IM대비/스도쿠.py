def sdoku(arr):
    N = 9
    dr = [0,1,1,1,0,-1,-1,-1]
    dc = [1,1,0,-1,-1,-1,0,1]
    mid = [1,4,7]
    for i in range(N):
        num = []
        for j in range(N):
            if arr[i][j] not in num:
                num.append(arr[i][j])
            else: continue
        if len(num) != 9: return 0
    for j in range(N):
        num = []
        for i in range(N):
            if arr[i][j] not in num:
                num.append(arr[i][j])
            else: continue
        if len(num) != 9: return 0
    for i in mid:
        for j in mid:
            num =[arr[i][j]]
            for k in range(8):
                nr = i + dr[k]
                nc = j + dc[k]
                if arr[nr][nc] not in num:
                    num.append(arr[nr][nc])
                else: continue
        if len(num) != 9: return 0

    return 1
T = int(input())
for tc in range(1,T+1):
    sdoku_array = [list(map(int, input().split())) for _ in range(9)]
    answer = sdoku(sdoku_array)
    print(f'#{tc} {answer}')
