def solution(triangle):
    print(len(triangle))
    value_list = []
    index = 0
    for i in range(len(triangle)):
        for j in range( len(triangle[i])+1):
            value_list.append(value_list[index:index + len(triangle[i])] )
            index += len(triangle[i])
    print(value_list)

    a = 0
    for i in range(0,len(triangle)):
        for j in range( len(triangle[i]) ):
            if i 
            print(triangle[i][j])

        # else:


    answer = 0
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)