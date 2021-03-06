"""
Q. 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?

8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)


#알고리즘의 컨셉: 10000개 까지 range로 돌리고 값을 string으로 바꾼다.
                그 다음에 길이를 재고 하나씩 분리해서 8 인지에 대해 확인한 후
                맞으면 카운트를 하는형식이다.


#조건 :1.1-10000 까지
       2.8의 숫자 카운팅

# 걸린 시간 : 13분 29초

# 느낀점 : 간단한 문제였는데 초반에 조금 멍때린 것 같다.
            str으로 바꾸면 길이를 잴 수 있고 하나씩 비교 할 수 있다는 걸 명심하자.
            그리고 for else 로 for 문이 종료 되면 else 문이 나오게 끔 만들었다. 파이썬에서만 가능하다.
"""

count = 0
for i in range(10000):
    str_i = str(i)
    for j in range(len(str_i)):
        if str_i[j] == '8':
            count += 1
else:
    print(count)

