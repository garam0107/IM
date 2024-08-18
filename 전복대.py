def pole(stack,A,B):
    cross = 0
    if not stack:
        stack.append([A,B])
    else:
        for i in range(len(stack)):
            if A > stack[i][0] and B < stack[i][1]:
                cross += 1
            elif A < stack[i][0] and B > stack[i][1]:
                cross += 1
        stack.append([A,B])
    return cross




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stack = []
    answer = 0
    for _ in range(N):
        A,B = map(int, input().split())
        answer += pole(stack,A,B)
    print(stack)
    print(f'#{tc} {answer}')



