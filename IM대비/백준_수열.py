def up(arr): # 연속해서 커질 때 구하는 함수
    max_v = 0
    sum = 1 # 최소 길이가 1이기 때문에 1로 설정한 길이 변수
    for i in range(N-1):
        if arr[i] <= arr[i+1]: # 다음 요소가 현재 요소 보다 크거나 같을 때
            sum += 1           # 길이 +1
        else:
            if sum > max_v: # 맥스값 보다 길이가 클 경우 맥스값 갱신
                max_v = sum
            sum = 1 # 다시 길이를 저장해야 하기 때문에 1로 초기화
    if sum > max_v: # 리스트를 다 순회한 후에도 현재 증가하는 부분의 길이가 맥스값 보다 클 경우 맥스값 갱신
        max_v = sum
    return max_v

def down(arr): # 연속해서 작아질 때 구하는 함수, 위의 함수에서 다음 요소가 현재 요소 보다 작을 경우의 조건만 바꿔줌
    max_v = 0
    sum = 1
    for i in range(N-1):
        if arr[i] >= arr[i+1]:
            sum += 1
        else:
            if sum > max_v:
                max_v = sum
            sum = 1
    if sum > max_v:
        max_v = sum
    return max_v

N = int(input())
num_list = list(map(int, input().split()))
print(max(up(num_list), down(num_list)))