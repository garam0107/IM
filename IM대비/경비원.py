def bouncer(W,L,N,arr,dir,dist): # W: 가로, L: 세로, arr: 마트 좌표 리스트 , dir,dist: 경비원 좌표
    total_dist = 0
    # 1: 북 , 2: 남, 3: 서 , 4: 동
    for i in range(N):
        if dir == arr[i][0]:                 # 같은 방향일 때는 경비원 위치에서 마트 위치 빼고 절댓값 씌우기
            total_dist += abs(dist-arr[i][1])
        elif dir == 1 and arr[i][0] == 2 or dir == 2 and arr[i][0] == 1:         # 북-남, 남-북 : 시계 방향과 반시계 방향중 최단 거리
            total_dist += min(L+dist+arr[i][1], L+(W-dist)+(W-arr[i][1]))
        elif dir == 1 and arr[i][0] == 3 or dir == 3 and arr[i][0] == 1:         # 서-북, 북-서 : 경비원 좌표 마트 좌표만 더해주면 됨
            total_dist += dist + arr[i][1]
        elif dir == 1 and arr[i][0] == 4:                   # 북-동: 가로 길이에서 경비원 좌표 뺀 값 + 마트 좌표
            total_dist += (W-dist) + arr[i][1]
        elif dir == 4 and arr[i][0] == 1:                   # 동-북: 위와 반대
            total_dist += (W-arr[i][1]) + dist
        elif dir == 2 and arr[i][0] == 3:                   # 남-서: 경비원 좌표 + 세로 길이에서 마트 좌표 뺀 값
            total_dist += dist + (L - arr[i][1])
        elif dir == 3 and arr[i][0] == 2:                   # 서-남: 위와 반대
            total_dist += arr[i][1] + (L-dist)
        elif dir == 2 and arr[i][0] == 4:                   # 남-동: 가로 길이에서 경비원 좌표 뺀 값 + 세로 길이에서 마트 좌표 뺀 값
            total_dist += (W-dist) + (L - arr[i][1])
        elif dir == 4 and arr[i][0] == 2:                   # 동-남: 위와 반대
            total_dist += (L - dist) + (W - arr[i][1])
        elif dir == 3 and arr[i][0] == 4 or dir == 4 and arr[i][0] == 3:    # 서-동, 동-서: 시계 방향과 반시계 방향 중 최단 거리
            total_dist += min(W+dist+arr[i][1], W+(L-dist)+(L-arr[i][1]))
    return total_dist


W,L = map(int, input().split())
count_mart = int(input())
mart = [list(map(int, input().split())) for _ in range(count_mart)]
dong_dir , dong_dist = map(int,input().split())
answer = bouncer(W,L,count_mart,mart,dong_dir,dong_dist)
print(answer)





