"""
-----------------------------------------------------------------------------------------------------------------------
2. [Spiral Array]

문제는 다음과 같다:
입력: 6, 6

 0   1   2   3   4   5
19  20  21  22  23   6
18  31  32  33  24   7
17  30  35  34  25   8
16  29  28  27  26   9
15  14  13  12  11  10

위처럼 6 6 이라는 입력을 주면 6 X 6 매트릭스에 나선형 회전을 한 값을 출력해야 한다.

 0   1   2   3   4   5
19  20  21  22  23   6
18  31  32  33  24   7
17  30  35  34  25   8
16  29  28  27  26   9
15  14  13  12  11  10

-----------------------------------------------------------------------------------------------------------------------
start : 12 시 40분
end :
"""
import numpy as np

#1.입력
# a = int(input())
# b = int(input())
a = 9
b = 9
z = []

# print(a)
# print(b)

#2.입력 받은 수에 대한 value 가져오기
value = [i for i in range(a*b)]
# print(value)

#3. 행렬 만들기

for i in range(0 , a):
    z.append(value[i*a:(i+1)*a])
print(z)

matrix = np.array([z[i] for i in range(0, a)])
# print(matrix)


x = 0
y = 0
left_right = 1
upper_lower = 0
break_x = 0
break_y = 1
break_c = 1
for i in range(a*b):
# 상하좌우로 갈 수 있는 수와 언제 방향이 바뀌는 지에 대해 정의 해야 된다.
# x가 작고 y 가 증가
# left_right = 1 일때 진행
    matrix[x][y] = i

    if x - break_x == 0 and y + break_y != b and y + break_y < b:
        upper_lower = 0
        left_right = 1
        y = y + left_right

    elif x + break_x == a and y != break_x - 1:
        upper_lower = 0
        left_right = -1
        y = y + left_right

    elif x != a and y + break_y == b:
        left_right = 0
        upper_lower = 1
        x = x + upper_lower

    elif x != a and y == break_x - 1:
        left_right = 0
        upper_lower = -1
        x = x + upper_lower

    if x + break_c == a and y + break_c == b:
        break_c = break_c + 1
        break_x = break_x + 1
        break_y = break_y + 1

print(matrix)


