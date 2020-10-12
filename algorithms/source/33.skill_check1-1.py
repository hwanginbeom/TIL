# 어떤 n 값이 들어왔을 때 n 값이 어떤 정수 x의 제곱인 경우 x+1의 제곱 값을
#반환하고, 그렇지 않은 경우 -1을 반환하는 문제이다.
def solution(n):
    a = str(n ** 0.5)
    if( a[(a.find("."))+1:] == '0' ):
        answer = ( float(a) +1)**2
    else:
        answer = -1return answer
