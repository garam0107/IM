def node(V,S,arr1):
    visited = [0]*(V+1)
    visited[S] = 1
    queue = [S]
    while queue:
        t = queue.pop(0)
        for i in arr1[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    return visited

T= int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adjl = [[] for _ in range(V+1)]
    for _ in range(E):
        x,y = map(int,input().split())
        adjl[x].append(y)
        adjl[y].append(x)
    S,G = map(int, input().split())
    final_list = node(V,S,adjl)
    answer = final_list[G] - 1
    if answer < 0: answer = 0
    print(f'#{tc} {answer}')








