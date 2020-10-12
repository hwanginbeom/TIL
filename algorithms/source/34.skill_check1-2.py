"""
2.문제
array값을 [1, 5, 2, 6, 3, 7, 4] 을받고 commands 값을 [[2, 5, 3], [4, 4, 1], [1, 7, 3]] 이렇게 받는다 이 경우에 commands [2, 5, 3] 이 
첫번째 값은   array의  시작 위치 - 5
두번째 값은 array가 끝나는 위치 - 3
세번째 값은 이 array값을 정렬 한 값에서 3번째 값 을 나타낸다. 
처음에 이걸하면 값은 [5,2,6,3] 에서 정렬한 후 
[2,3,5,6] 에서  3번째 값을 뽑으면 값이 5가 나온다. 이 경우의 함수를 만드는 문제였다.
"""

def solution(array, commands):
    array=array
    answer = []
    for i in range(0,len(commands)):
        a=sorted(array[ (commands[i][0])-1:(commands[i][1])] )
        answer.append(a[(commands[i][2])-1])
    return answer
