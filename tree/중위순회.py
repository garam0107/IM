def order(node):
    if node > N:
        return
    order(node*2)
    inorder.append(node)
    order(node*2+1)



T = 10
for tc in range(1,T+1):
    N = int(input())
    tree_data = [0] * (N+1)
    for _ in range(N):
        array = list(input().split())
        tree_data[int(array[0])] = array[1]

    inorder = []
    order(1)
    print(f'#{tc}',end=' ')
    for i in inorder:
        print(tree_data[i], end='')
    print()



