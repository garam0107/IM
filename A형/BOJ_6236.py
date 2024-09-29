def money():
    global low,high
    result = 0 # K원 저장
    while low <= high:
        mid = (low+high) // 2
        total_money = 0 # 수중에 있는 돈
        cnt = 0 # 인출 횟수
        for m in money_list:
            if total_money + m <= mid: # 현재 인출 금액 + 하루치 금액이 mid를 넘지 않으면
                total_money += m       # 돈을 수중에 추가
            else:  # 아니면
                cnt += 1   # 인출 횟수 +1
                total_money = m  # 하루치 금액으로 초기화
        # 마지막 날 돈이 남아 있으면 써야하니까 인출 횟수 +1
        if total_money > 0:
            cnt += 1
        if cnt > M: # 인출 횟수가 M보다 많으면 인출 금액 늘리기
            low = mid + 1
        else: # 아니면 인출 금액 줄이기
            high = mid - 1
            result = mid

    return result

N,M = map(int, input().split())
money_list = [int(input()) for _ in range(N)]
low = max(money_list)  # K의 최솟값은 써야 하는 금액중 최댓값
high = sum(money_list)  # 모든 돈을 한 번에 뽑아서 다 쓰는 경우가 K의 최댓값
answer = money()
print(answer)

