import sys
sys.stdin = open('input (3).txt','r')
def find_idx(r,c,arr):
    idx_r,idx_c = 0,0
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            if arr[i][j] == 1:
                idx_r = i
                idx_c = j
                break
    return idx_r,idx_c
def password(arr):
    r,c = find_idx(row,col,array)
    password_list = [[0]*7 for _ in range(8)]
    for i in range(7,-1,-1):
        for j in range(6,-1,-1):
            password_list[i][j] = arr[r][c]
            c -= 1
    return password_list
T = int(input())
for tc in range(1,T+1):
    row,col = map(int,input().split())
    array = [list(map(int,input())) for _ in range(row)]
    password_code = [[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],
                     [0,1,0,0,0,1,1],[0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],
                     [0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
    final = password(array)
    for idx in range(8):
        for i in range(10):
            if final[idx] == password_code[i]:
                final[idx] = i
                break
    final.insert(0,0)
    odd = 0
    even = 0
    for i in range(1,9):
        if i % 2 == 0:
            even += final[i]
        else:
            odd += final[i]
    total = odd * 3 + even
    answer = 0
    if total % 10 == 0:
        answer = sum(final)

    print(f'#{tc} {answer}')





