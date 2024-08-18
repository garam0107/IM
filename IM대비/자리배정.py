def choose_chair(row,col,num,arr):
    counts = 1
    r = 5
    c = 0
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    arr[r][c] = 1
    while counts < row*col:
        counts += 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if k == 0:
                while 0 <







C,R = map(int, input().split())
k_num = int(input())
chair_list = [[0]*C for _ in range(R)]
