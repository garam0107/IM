
def candidate():
    queue = []
    for i in array:
        if len(queue) < N:
            if i not in queue:
                queue.append(i)
                student[i] += 1
            else:
                student[i] += 1
        else:
            if i not in queue:
                like = []
                for j in queue:
                    like.append(student[j])
                min_i = like.index(min(like))
                student[queue[min_i]] = 0
                queue.pop(min_i)
                queue.append(i)
                student[i] += 1
            else:
                student[i] += 1
    return queue





N = int(input())
total_like = int(input())
array = list(map(int, input().split()))
student = [0] * 101
answer = candidate()
result = sorted(answer)
print(*result)
