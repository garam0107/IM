# import sys
# sys.stdin = open('sample_input (2).txt','r')

def build_row(N,l,arr):
    global total
    for i in range(N):
        same = 1
        for j in range(N-1):
            if arr[i][j] > arr[i][j+1] :
                counts = 1
                builted_row[i][j+1] = arr[i][j+1]
                for idx in range(1,l+1):
                    if j+1+idx < N and arr[i][j+1+idx] == arr[i][j+1]:
                        counts += 1
                        builted_row[i][j+1+idx] = arr[i][j+1]
                    if counts == l:
                        break
            elif arr[i][j] == arr[i][j+1]:
                same += 1

        if same == N:
            total += 1
    for i in range(N):
        for j in range(N-1,0,-1):
            if arr[i][j] > arr[i][j-1] and builted_row[i][j-1] == 0:
                counts = 1
                builted_row[i][j-1] = arr[i][j-1]
                for idx in range(1, l + 1):
                    if j-1-idx >= 0 and arr[i][j-1-idx] == arr[i][j-1]:
                        counts += 1
                        builted_row[i][j-1-idx] = arr[i][j-1]
                    if counts == l:
                        break
            elif arr[i][j] > arr[i][j-1] and builted_row[i][j-1] != 0:
                builted_row[i][j-1] = 0
    return builted_row

def build_col(N,l,arr):
    global total
    for j in range(N):
        same = 1
        for i in range(N-1):
            if arr[i][j] > arr[i+1][j]:
                counts = 1
                builted_col[i+1][j] = arr[i+1][j]
                for idx in range(1,l+1):
                    if i+1+idx < N and arr[i+1+idx][j] == arr[i+1][j]:
                        counts += 1
                        builted_col[i+1+idx][j] = arr[i+1][j]
                    if counts == l:
                        break
            elif arr[i][j] == arr[i+1][j]:
                same += 1
        if same == N:
            total += 1

    for j in range(N):
        for i in range(N-1,0,-1):
            if arr[i][j] > arr[i-1][j]  and builted_col[i-1][j] == 0:
                counts = 1
                builted_col[i-1][j] = arr[i-1][j]
                for idx in range(1, l + 1):
                    if i-1-idx >= 0 and arr[i-1-idx][j] == arr[i-1][j]:
                        counts += 1
                        builted_col[i-1-idx][j] = arr[i-1][j]
                    if counts == l:
                        break
            elif arr[i][j] > arr[i-1][j]  and builted_col[i-1][j] != 0:
                builted_col[i-1][j] = 0
    return builted_col

def count_build(N,l):
    global total
    arr1 = build_row(N,length,array)
    arr2 = build_col(N,length,array)
    print(arr1)
    print(arr2)
    for i in range(N):
        same_1 = []
        result = 1
        for j in range(N-1):
            if arr1[i][j] == 0 : continue
            elif arr1[i][j] == arr1[i][j+1]:
                result += 1
            else:
                same_1.append(result)
                result  = 1
        if arr1[i][N-1] != 0:
            same_1.append(result)
        print(same_1)
        flag = True
        if not same_1: flag = False
        for i in same_1:
            if i != l: flag = False
        if flag == True: total += 1

    for idx in range(N):
        same_2 = []
        result = 1
        for jdx in range(N-1):
            if arr2[jdx][idx] == 0 : continue
            elif arr2[jdx][idx] == arr2[jdx+1][idx]:
                result += 1
            else:
                same_2.append(result)
                result = 1
        if arr2[N-1][idx] != 0:
            same_2.append(result)
        print(same_2)
        flag = True
        if not same_2: flag = False
        for i in same_2:
            if i != l: flag = False
        if flag == True: total += 1


T = int(input())
for tc in range(1,T+1):
    N,length = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    builted_row = [[0]*N for _ in range(N)]
    builted_col = [[0]*N for _ in range(N)]
    total = 0
    count_build(N,length)
    print(total)

