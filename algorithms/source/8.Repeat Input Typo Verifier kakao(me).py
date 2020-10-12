"""
[반복입력 오타 검증기]
kakao 라고 타이핑을 쳐야하지만 키보드가 오작동하는 탓인지 같은 문자가 반복해서 찍히는 경우가 있다
예를들어 kakao -> kkakaoo 이런경우 반복입력이 되었다고 하고 True를 내보내는 function을 작성하자
(단, 글자가 안쳐져서 뺴먹지는 않는다고 가정 kkao 이런것은 불가능)

문자를 하나씩 계속 비교하고 만약 다르면 앞에 꺼랑 같은지 확인한다.

#알고리즘의 컨셉
입력 받는 값과 답을 나눠서 배열에 넣는다.
배열에 넣은후 하나씩 비교한다.
만약 다를 경우에는 답의 그 전 문자와 i번째 입력받은 문자와 같은 지 비교를 통해 중복을 넘긴다.
이런식으로 쭉 진행한다.



#조건 : 1.입력받는다.
        2.각 단어를 비교 해야한다.
        3.중복 되는건 상관없다.


# 걸린 시간 : 56분 34초


# 느낀점 : 문제가 애매모호해서 처음에 쫌 해맸다. 같은 값을 비교하는 것 까지는 쉽게 갔다.
            하지만 입력받는 값이 늘어나고 정답은 고정되어 있는 부분에서 막혀서 쫌 오래 걸린 것 같다.
            배열을 좀 시각화 해서 볼 수 있는 능력이 필요하다.
"""


def test(value, in_str):
    value2 = []
    in_str2 = []
    a = 0

    for i in range(len(value)):
        value2 += value[i]

    for i in range(len(in_str)):
        if len(value2) > a:
            if value2[a] == in_str[i]:
                in_str2 += in_str[i]
                a += 1
                continue
            elif value2[a-1] == in_str[i]:
                continue
            else:
                in_str2 += '@'
        elif in_str[i - 1] == in_str[i]:
            continue
        else:
            in_str2 += '@'

    if value2 == in_str2:
        print('멀쩡함')
    else:
        print('다른 글자!!!!')



test('kkakaoo', 'kkkaaooooo')