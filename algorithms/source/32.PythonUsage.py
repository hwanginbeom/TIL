#1.몫과 나머지 - divmod

#일반적인 문법
a = 7
b = 5
print(a//b, a%b)
#python 함수
a = 7
b = 5
print( *divmod(a, b))


#2.n진법으로 표기된 string을 10진법 숫자로 변환하기 - int 함수

num = '3212'
base = 5

answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )

num = '32122'
base = 10
answer = int(num, base)
print(answer)

#3.문자열 정렬하기 - ljust, center, rjust

### 우측 정렬 예
s = '가나다라'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s

#정렬 사용
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬


#4.알파벳 출력하기 - string 모듈

import string

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789


#5.2차원 리스트 뒤집기 - ⭐️zip⭐️

#2차원 리스트 뒤집기
def solution(mylist):
    answer=[]
    b=[]
    for i in range(1,len(mylist)+1):
        for j in range(1,len(mylist)+1):
            b.append(mylist[j-1][i-1])
        answer.append(b)
        b=[]
    return answer

mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = [[],[],[]]

for i in range(3):
    for j in range(3):
        new_list[i].append( mylist[j][i] )


mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))