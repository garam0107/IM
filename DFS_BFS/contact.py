import sys
sys.stdin = open('input (2).txt','r')
def contact(N,S,array):
    visited = [0] * (N+1)
    visited[S] = 1
    queue = [S]
    while queue:
        t = queue.pop(0)
        for i in array[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    return visited
def final():
    final_list = contact(N,S,al)
    find = max(final_list)
    max_list = []
    for i in range(len(final_list)):
        if final_list[i] == find:
            max_list.append(i)
    return max(max_list)
T = 10
for tc in range(1,T+1):
    L,S = map(int,input().split())
    N = 100
    al = [[] for _ in range(N+1)]
    array = list(map(int,input().split()))
    for i in range(0,L,2):
        x,y = array[i],array[i+1]
        if y not in al[x]:
            al[x].append(y)
    answer = final()
    print(f'#{tc} {answer}')
