def back(N,array):
    counts = 0
    stack = [(array[0],array[1])]
    




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    back_room = [list(map(int,input().split())) for _ in range(N)]

