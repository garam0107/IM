def move(N,K,array):
    start = 1 # 문제에서 1부터 시작이기에 start를 1로 설정
    food_idx = [] # 먹이가 있는 인덱스를 저장하기 위한 리스트
    if array[0] == 0: # 첫번째 요소가 0이면 첫번째 칸에서 그대로 멈추니까 1을 반환
        return 1
    for i in range(N):
        if array[i] == 1:
            food_idx.append(i) # 먹이가 있는 인덱스 저장
    if len(food_idx) == 1:
        return K+1
    for i in range(1,len(food_idx)):  # 현재 요소랑 다음 요소의 차이를 비교하기 위해 1부터 시작
        if food_idx[i] - food_idx[i-1] <= K:
            start = food_idx[i]+1 # 현재 먹이가 있는 인덱스와 다음 먹이의 인덱스의 차이가 k 이하이면 start를 food_idx[i]의 값에서 1을 더한 값으로 설정
            start += K # 현재 위치인 start에서 K만큼 더해주기
        elif food_idx[i] - food_idx[i-1] > K:
            start = food_idx[i-1]+1 # 현재 먹이가 있는 인덱스와 다음 먹이의 인덱스의 차이가 k보다 크면 start를 현재 먹이의 인덱스인 food_idx[i-1]의 값에서 1을 더한 값으로 설정
            start += K  # 현재 위치인 start에서 K만큼 더해주고 for문 중단
            break


    if start >= N: # 현재 위치의 값이 N 이상일 경우 최대 N까지만 갈 수 있으므로 N으로 설정
        start = N
    return start



T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    food_array = list(map(int, input().split()))
    answer = move(N,K,food_array)
    print(f'#{tc} {answer}')