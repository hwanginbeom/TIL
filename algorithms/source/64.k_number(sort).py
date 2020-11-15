# 9분
def solution(array, commands):
    result=[]
    for i in commands:
        answer = array[i[0]-1:i[1]]
        answer.sort()
        result.append(answer[i[2]-1])
    return result

array = [1, 5, 2, 6, 3, 7, 4]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array, commands)