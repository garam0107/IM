import sys
sys.stdin = open('input (3).txt','r')
def postorder(node):
    if not graph[node]:
        return int(root[node])

    left = postorder(graph[node][0])
    right = postorder(graph[node][1])

    if root[node] == '+':
        return left + right
    elif root[node] == '-':
        return left - right
    elif root[node] == '*':
        return left * right
    elif root[node] == '/':
        return left / right



for tc in range(1,11):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    root = [''] * (N+1)
    four = ['+','*','-','/']
    for _ in range(N):
        temp = input().split()
        node = int(temp[0])
        root[node] = temp[1]
        if len(temp) == 4:
            graph[node].append(int(temp[2]))
            graph[node].append(int(temp[3]))

    answer = int(postorder(1))
    print(f'#{tc} {answer}')

