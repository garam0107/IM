def ruins(array,N,M):
    max_v = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if array[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0
    return max_v
def ruins2(array,N,M):
    max_v = 0
    for j in range(M):
        cnt = 0
        for i in range(N):
            if array[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0
    return max_v






T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    answer = max(ruins(array,N,M), ruins2(array,N,M))
    print(f'#{tc} {answer}')