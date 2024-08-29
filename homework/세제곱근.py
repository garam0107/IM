# def three(N,arr):
#     global answer
#     for i in arr:
#         div = N / i
#         if int(div) * i == N:
#             answer.append(i)
#             three(int(div),arr)
#     return answer
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     result = -1
#
#     for i in range(1,N//4):
#         if i**3 == N:
#             result = i
#             break
#     print(f'#{tc} {result}')
a = 123406009809
result = -1
for i in range(1,1000000):
    if a == i**3:
        result = i
        break
print(result)
print(12345**3)