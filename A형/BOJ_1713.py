
def candidate():
    queue = [] # 사진틀 리스트, (queue 이용할려 했는데 굳이 필요없음)
    for i in array:
        if len(queue) < N:  # 아직 사진틀이 비어있을 때
            if i not in queue:  # 추천 받은 학생이 사진틀에 없으면
                queue.append(i)  # 리스트에 추가
                student[i] += 1  # 추천 횟수 + 1
            else:    # 사진틀에 있으면 추천 횟수만 +1
                student[i] += 1
        else: # 사진틀이 꽉 차면
            if i not in queue: # 추천 받은 학생이 사진 틀에 없으면 사진틀에서 1명 삭제
                like = [] # 사진틀에 있는 학생들의 추천 횟수 저장
                for j in queue:
                    like.append(student[j])
                min_i = like.index(min(like))  # 추천 횟수 젤 적은 사람의 인덱스
                student[queue[min_i]] = 0 # 추천 횟수 0으로 초기화 후 사진틀에 추가 후 사진틀에서 삭제
                queue.pop(min_i)
                queue.append(i)
                student[i] += 1
            else:
                student[i] += 1
    return queue





N = int(input())
total_like = int(input())
array = list(map(int, input().split()))
student = [0] * 101 # ' '번 학생의 추천 횟수 저장
answer = candidate()
result = sorted(answer)
print(*result)
