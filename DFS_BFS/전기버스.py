def elec_bus(K,N,M,array):
    last = array[M-1]
    first = array[0]
    if N - last > K or first > K:
        return 0
    for i in range(1,M):
        if array[i]-array[i-1] > K:
            return 0
    counts = 0
    elec = 0
    final_list = [0] + array + [N]
    for i in range(len(final_list)-1):
        elec += final_list[i+1] - final_list[i]
        if elec > K:
            counts += 1
            elec = final_list[i+1] - final_list[i]
    return counts



T = int(input())
for tc in range(1,T+1):
    K,N,M = map(int,input().split())
    bus_list = list(map(int,input().split()))
    answer = elec_bus(K,N,M,bus_list)
    print(f'#{tc} {answer}')


