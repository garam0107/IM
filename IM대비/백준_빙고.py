def bingo_count(N,arr2,arr1):
    counts = 0
    for i in range(N):
        for j in range(N):
            if arr1[i] == arr2[i][j]:
                arr2[i][j] = 0
                counts += 1
    return counts

def three_bingo(counts, N,arr):
    bingo = 0
    if counts >= 12:
        for i in range(N):
            if arr[i].count(0) == 5:
                bingo += 1
        for i in range(N):
            c = 0
            for j in range(N):
                if arr[j][i] == 0:
                    c += 1
                    if c == 5:
                        bingo += 1
        for i in range(N):
            c = 0
            if arr[i][i] == 0:
                c += 1
                if c == 5:
                    bingo += 1
        for i in range(N):
            c = 0
            if arr[i][N-i-1] == 0:
                c += 1
                if c == 5:
                    bingo += 1
                    if bingo == 3:
                        return counts
                    elif bingo < 3:
                        bingo = 0

N = 5
bingo = [list(map(int,input().split())) for _ in range(N)]
answer = 0
for _ in range(N):
    talk = list(map(int,input().split()))
    counts = bingo_count(N,talk,bingo)
    answer = three_bingo(counts,N,bingo)

print(answer)


