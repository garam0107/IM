T = int(input())
for tc in range(1,T+1):
    array = list(input())
    cnt = 0
    for i in range(len(array)-1):
        if array[i] == '(' and array[i+1] == ')':
            cnt += 1
        elif array[i] == '(' and array[i+1] != ')':
            cnt += 1
        elif array[i] == '|' and array[i+1] == ')':
            cnt += 1

    print(cnt)

