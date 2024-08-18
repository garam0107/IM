def box(box,L, R, i):
    a = L-1
    b = R
    for idx in range(a,b):
        box[idx] = str(i)
    return box

T = int(input())
for tc in range(1,T+1):
    N,Q = map(int, input().split())
    box_num = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        box(box_num,L,R,i)
    print(f'#{tc}', *box_num)




