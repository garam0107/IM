def janghun(N,H,array):
    people_sum = sum(array)
    if people_sum == H:
        return 0
    hap_list = []
    for i in range(N):
        result = people_sum-array[i]
        if result < H: continue
        elif result >= H:
            hap_list.append(H-result)
    


T = int(input())
for tc in range(1,T+1):
    N,high = map(int,input().split())
    height_list = list(map(int,input().split()))
