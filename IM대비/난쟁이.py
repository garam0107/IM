def nine(array):
    result = 100
    num_list = []   # 9개의 인덱스 중 2개를 고르는 모든 경우의 수를 리스트에 추가, 9C2
    for i in range(9):
        for j in range(i+1,9):
            num_list.append([i,j])

    for A,B in num_list:
        sum_list = [] # 난쟁이의 키를 담을 리스트
        sum = 0   # 난쟁이의 키를 더할 변수
        for i in range(9): # 2개의 인덱스를 제외하고 나머지 7개의 요소만 탐색
            if A == i : continue
            if B == i : continue
            sum += array[i]
            sum_list.append(array[i])
            if len(sum_list) == 7 and sum == result: # 난쟁이가 7명이고 합이 100이면 리스트 난쟁이의 키 리스트 반
                return sum_list




dwarf = []
for _ in range(9):
    height = int(input())
    dwarf.append(height)
answer = nine(dwarf)
final_answer = sorted(answer)
for seven in final_answer:
    print(seven)



