def solution(array, commands):
    b=[]
    for i in range(0,len(commands)):
        answer=array[ (commands[i][0])-1: (commands[i][1])]
        answer.sort()
        print(answer)
        b.append(answer[ (commands[i][2])-1 ])
        print(b)

    print(answer)
    return answer


def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


solution(array, commands)