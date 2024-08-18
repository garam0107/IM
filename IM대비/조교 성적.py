def rank(score_list, score):  # 기말, 중간, 과제 점수를 비율에 맞춰서 곱해서 합한 점수를 리스트로 만듬
    total = 0.35 * score[0] + 0.45 * score[1] + 0.2 * score[2]
    score_list.append(total)
    return score_list




T = int(input())
for tc in range(1, T+1):
    student, s_num = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+','B0','B-','C+','C0','C-','D0']  # 등급 리스트
    score_list = [] # rank함수 실행해서 나오는 총점 저장할 리스트
    for _ in range(student):
        score = list(map(int, input().split()))
        rank(score_list,score)
    final_score_list = sorted(score_list, reverse=True) # 총점 리스트를 내림차순으로 정렬해야 등급 매길 수 있음
    index = 0 # s_num번째 학생의 점수와 정렬된 총점 리스트를 비교하여 해당 학생의 인덱스를 찾
    for i in range(student):
        if score_list[s_num-1] == final_score_list[i]: # 1번째 학생부터 시작하기에 s_num에 -1
            index = i
            break

    x = student // 10
    answer = grade[index // x]
    print(f'#{tc} {answer}')

    # 학생 수를 10으로 나눈 횟수가 등급마 중복될 수 있는 횟수
    # 찾은 인덱스를 횟수로 나누어 해당 학생의 등급을 결정, 예를 들어 학생수가 20이면 각 등급이 2번씩 나올 수 있는 것
    # 그렇기에 01 ,23, 45 ... 순으로 등급이 정해짐, 찾은 인덱스가 4면 4//2인 2의 값이 그 학생의 등급





