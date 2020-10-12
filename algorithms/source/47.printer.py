def solution(priorities, location):
    answer = 0
    max_prioritie = max(priorities)
    while True:
        prioritie_value = priorities.pop(0)
        if max_prioritie == prioritie_value:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_prioritie = max(priorities)
        else:
            priorities.append(prioritie_value)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1

    return answer

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))