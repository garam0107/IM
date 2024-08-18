
# array = card 리스트, N = card 리스트 요소 개수
def shuffle(array, N):
    list_1 = []    # 카드 리스트를 2개에 나누어 저장
    list_2 = []
    num = N // 2
    # 카드 개수가 짝수일 때는 똑같은 장수로 나누어 지고 홀수일 때는 첫번 째 리스트에 1장을 더 추가
    if N % 2 == 0:
        for i in range(num):
            list_1.append(array[i])
        for idx in range(num,N):
            list_2.append(array[idx])
    else:
        for i in range(num+1):
            list_1.append(array[i])
        for idx in range(num+1, N):
            list_2.append(array[idx])
    final_card = [] # 리스트1,2에서 한 장씩 꺼내서 저장할 리스트
    for i in range(num): #리스트1,2에서 처음 넣은 것을 하나씩 꺼내서 final_card에 추가
        final_card.append(list_1.pop(0))
        final_card.append(list_2.pop(0))
    if list_1: # 만약 리스트1에 요소가 남아있다면 카드 개수가 홀수인 경우라 1장이 남아있는 경우고 남은 1장을 final_card에 추가
        final_card.append(list_1[0])
    return final_card



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(map(str, input().split()))
    answer = shuffle(card,N)
    print(f'#{tc}', *answer)


