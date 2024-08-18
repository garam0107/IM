def black_paper(N, arr1,arr2):
    num = 100
    length = 10 # 색종이의 가로,세로 길이
    for i in range(N):
        r = arr1[i][0] # 왼쪽에서부터 떨어진 거리
        c = arr1[i][1] # 아래로부터 떨어진 거리
        for col in range(num - c - length, num - c): #색종이의 범위만큼 1로 덮기
            for row in range(r,r+length):
                if arr2[col][row] == 0: # 도화지가 0일 경우 안겹치는 곳이기 때문에 1
                    arr2[col][row] = 1
                elif arr2[col][row] == 1: # 도화지가 1일 경우 겹치는 곳이기 때문에 넘어가기
                    continue
    return arr2


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white_paper = [[0]*100 for _ in range(100)] # 100X100 2차원 도화지 리스트
black_paper(N,paper,white_paper)
answer= 0
for i in range(100): # 색종이로 범위를 1로 바꿔놨기 때문에 1의 개수가 색종이가 붙은 부분의 넓이
    for j in range(100):
        if white_paper[i][j] == 1:
            answer += 1
print(answer)


