T = int(input())
for tc in range(1,T+1):
    len_road = int(input())
    road = list(map(int, input().split()))

    road_list = [road[0]]
    total = []
    for i in range(len_road-1):
        if road[i] <= road[i+1]:
            road_list.append(road[i+1])
        else:
            if len(road_list) >= 2:
                total.append([len(road_list), (road_list[-1] - road_list[0])/len(road_list)])
                road_list = []
                road_list.append(road[i+1])

    if len(road_list) >=2 :
        total.append([len(road_list), (road_list[-1] - road_list[0])/len(road_list)])


    a = 100
    result = 0
    if total:
        for idx in range(len(total)):
            if total[idx][1] < a:
                a = total[idx][1]
                result = total[idx][0]
            elif total[idx][1] == a:
                if result < total[idx][0]:
                    result = total[idx][0]

    else:
        result = 0

    print(f'#{tc} {result}')











