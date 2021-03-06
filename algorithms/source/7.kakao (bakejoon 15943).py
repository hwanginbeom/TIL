

"""
카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.

순위	상금	인원
1등	500만원	1명
2등	300만원	2명
3등	200만원	3명
4등	50만원	4명
5등	30만원	5명
6등	10만원	6명
2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.

순위	상금	인원
1등	512만원	1명
2등	256만원	2명
3등	128만원	4명
4등	64만원	8명
5등	32만원	16명


# 첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 T(1 ≤ T ≤ 1,000)가 주어진다.


# 다음 T개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다. 각 줄에는 두 개의 음이 아닌 정수 a(0 ≤ a ≤ 100)와 b(0 ≤ b ≤ 64)가 공백 하나를 사이로 두고 주어진다.


#조건 : 1.첫번쨰 입력
        2.입력해서 띄어쓰기로 구분해서 나누기
        3.등수에 맞춰서 상금 나누기


# 걸린 시간 : 21분 34초



# 느낀점 : 마지막에 return 에 값이 없을 경우에 0을 안처리해서 안됐었다. 주의 하자 validation 하자 !
            문제 자체가 생각 할 껀 딱히 없없다. 조건을 하나씩 찾아서 정리하는 느낌으로 하면 될 것 같다.
            시간을 쫌 줄여야 겠다. 간단한 하드코딩인데 시간이 쫌 걸렸다.
"""



def ranking_2017(a):
    if a==1:
        return 5000000
    elif 1 < a <= 3:
        return 3000000
    elif 3 < a <= 6:
        return 2000000
    elif 6 < a <= 10:
        return 500000
    elif 10 < a <= 15:
        return 300000
    elif 15 < a <= 21:
        return 100000
    else:
        return 0


def ranking_2018(a):
    if a==1:
        return 5120000
    elif 1 < a <= 3:
        return 2560000
    elif 3 < a <= 7:
        return 1280000
    elif 6 < a <= 15:
        return 640000
    elif 10 < a <= 31:
        return 320000
    else:
        return 0


first = int(input()) # 숫자로 입력 받기

for i in range(first):
    second = input()
    second_1 = int(second.split(' ')[0])
    second_2 = int(second.split(' ')[1])
    print(ranking_2017(second_1)+ranking_2018(second_2))

"""
6
8 4
13 19
8 10
18 18
8 25
13 16
"""


