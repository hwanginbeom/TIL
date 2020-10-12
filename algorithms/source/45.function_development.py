def solution(progresses, speeds):
    queue = []
    for i in range(0, len(speeds)):
        if (100 - progresses[i]) % speeds[i] == 0:
            queue.append((100 - progresses[i]) / speeds[i])
        else:
            queue.append(round((100 - progresses[i]) / speeds[i], 0) + 1)
    print(queue)
    max_value = 0
    count = 0
    answer = []
    for i in range(0, len(queue)):
        count += 1
        if max_value < queue[i] and i != 0:
            max_value = queue[i]
            answer.append(count)
            count = 0

    return answer


def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    print(Q)
    return [q[1] for q in Q]

progresses = [93, 30, 55, 55]

speeds = [1, 30, 5, 4]

print(solution2(progresses, speeds))
print(solution(progresses, speeds))


