# import sys
# sys.stdin = open('input (1).txt', 'r')
def Bread(N, arr, second, bread):   # 정렬을 안하고 풀어서 30번 케이스 1개가 안풀림 !!!!!!
    for i in range(N):
        if arr[i] < second:
            return 'Impossible'
    bread_list = 0
    for _ in range(second, max(arr)+1, second):
        bread_list += bread
    for idx in range(N):
        if arr[idx] >= second:
            bread_list -= (arr[idx] // second) * bread
        elif bread_list <= 0:
            return 'Impossible'

    return 'Possible'


T = int(input())
for tc in range(1, T + 1):
    N, second, bread = map(int, input().split())
    people = list(map(int, input().split()))
    answer = Bread(N, people, second, bread)
    print(f'#{tc} {answer}')