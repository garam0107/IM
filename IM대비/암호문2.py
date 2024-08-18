T = 10
for tc in range(1,T+1):
    len_password = int(input())
    origin_password = list(map(int, input().split()))
    count_command = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            add_idx = int(command[i+1])  # 숫자를 삽입할 인덱스
            len_idx = int(command[i+2])  # 인덱스로부터 몇 개의 숫자를 삽입할지 정할 변수
            for idx in range(len_idx): # 삽입할 숫자의 개수만큼 반복
                origin_password.insert(add_idx+idx,command[i+2+idx+1]) # 해당 위치에 숫자 삽입

        elif command[i] == 'D':
            pop_idx = int(command[i+1])  # 제거할 인덱스의 위치
            len_idx = int(command[i+2])  # 삭제할 숫자의 개수
            for _ in range(len_idx): # 삭제할 개수 만큼 반복
                origin_password.pop(pop_idx)
    answer = origin_password[:10]
    print(f'#{tc}', end=' ')
    print(*answer)





