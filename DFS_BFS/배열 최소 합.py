# 최소 비용을 찾기 위한 전역 변수
def find_min(x, sum_v):
    global min_sum

    # 현재까지의 비용이 현재 최솟값보다 크거나 같으면 더 이상 탐색하지 않음
    if sum_v >= min_sum:
        return

    # 모든 행을 처리한 경우 (기저 조건)
    if x == N:
        # 현재까지의 비용이 최소 비용보다 작으면 갱신
        if min_sum > sum_v:
            min_sum = sum_v
            return

    # 각 열을 순회하며 가능한 선택을 시도
    for i in range(N):
        # 열이 아직 사용되지 않은 경우
        if not col[i]:
            # 해당 열을 사용 표시
            col[i] = 1
            # 다음 행으로 넘어가며 재귀 호출
            find_min(x + 1, sum_v + arr[x][i])
            # 해당 열의 사용을 해제 (백트래킹)
            col[i] = 0


# 테스트 케이스 수 입력
T = int(input())
# 각 테스트 케이스에 대해 반복
for tc in range(1, T + 1):
    # 배열의 크기 N 입력
    N = int(input())
    # N x N 배열 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최솟값을 초기화 (굉장히 큰 값으로 시작)
    min_sum = 100000000
    # 각 열의 사용 여부를 저장할 리스트
    col = [0] * N

    # 백트래킹을 통한 최소 비용 찾기
    find_min(0, 0)

    # 결과 출력
    print(f'#{tc} {min_sum}')

