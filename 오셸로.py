def black(field, arr, N):
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    r, c = arr[0], arr[1]
    field[r][c] = 1

    for k in range(8):
        plus = []
        for add in range(1, N + 1):
            nr = r + dr[k] * add
            nc = c + dc[k] * add
            if not (1 <= nr <= N  and 1 <= nc <= N):
                break
            if field[nr][nc] == 0:
                break
            if field[nr][nc] == 1:
                for Nr, Nc in plus:
                    field[Nr][Nc] = 1
                break
            plus.append((nr, nc))

def white(field, arr, N):
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    r, c = arr[0], arr[1]
    field[r][c] = 2

    for k in range(8):
        plus = []
        for add in range(1, N + 1):
            nr = r + dr[k] * add
            nc = c + dc[k] * add
            if not (1 <= nr <= N and 1 <= nc <= N):
                break
            if field[nr][nc] == 0:
                break
            if field[nr][nc] == 2:
                for Nr, Nc in plus:
                    field[Nr][Nc] = 2
                break
            plus.append((nr, nc))


def oselro(field, arr, N):
    if arr[2] == 1:
        black(field, arr, N)
    elif arr[2] == 2:
        white(field, arr, N)
    return field


T = int(input())
for tc in range(1, T + 1):
    N, stage = map(int, input().split())
    field = [[0] * (N + 2) for _ in range(N + 2)]
    x = N // 2
    y = N // 2 + 1
    field[x][x] = 2
    field[y][y] = 2
    field[x][y] = 1
    field[y][x] = 1
    for _ in range(stage):
        play = list(map(int, input().split()))
        oselro(field, play, N)
    white = 0
    black = 0
    for i in range(1, N + 1):
        white += field[i].count(2)
        black += field[i].count(1)
    print(f'#{tc} {black} {white}')
