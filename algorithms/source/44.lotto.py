# 문제 3.
# 로또 프로그램 작성
# 5000원으로 로또복권을 5장 자동으로 구매합니다.
# 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
# 쉬운버전으로 먼저 작성합니다.
# 6숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.
# 즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
# 쉬운버전을 해결했다면
# 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
# 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등,
# 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등,
# 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.

# 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
# 4등 몇개, 꽝 몇개로 출력
# 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개,
# 4등 몇개, 5등 몇개, 꽝 몇개로 출력

# 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
import random

win_number = random.sample(range(1, 45), 6)
# print(win_number)
my_number = []
for i in range(5):
    my_number.append(random.sample(range(1, 45), 6))

my_number[0] = win_number
# print(my_number)
count = []
count_num = 0
count_one = 0
for i in range(5):
    count_one = 0
    for j in range(6):
        for z in range(6):
            count_num = 0
            if my_number[i][j] == win_number[z]:
                count_num += 1
            count_one += count_num
    count.append(count_one)
# print(count)

one = 0
two = 0
thr = 0
four = 0
fail = 0
for i in count:
    if i == 6:
        one += 1
    elif i == 5:
        two += 1
    elif i == 4:
        thr += 1
    elif i == 3:
        four += 1
    else:
        fail += 1
print("문제 3번 (쉬운버전) : 1등 {}개, 2등 {}개, 3등 {}개, 4등 {}개, 탈락 {} 입니다.".format(one, two, thr, four, fail))


### 보너스 문제
win_number = random.sample(range(1, 45), 7)
win_number_ori = win_number[0:6]
win_number_bon = win_number[0:7]
# print(win_number_bon)
# print(win_number_ori)
# print(win_number)
my_number = []
for i in range(5):
    my_number.append(random.sample(range(1, 45), 6))

my_number[0] = win_number_ori # 1등 일 때
my_number[1] = win_number_bon[1:7] # 2등 일때
# print(my_number)
count_ori = []
count_num_ori = 0
count_one_ori = 0
count_bon = []
count_num_bon = 0
count_one_bon = 0

for i in range(5):
    count_one_ori = 0
    count_one_bon = 0
    for j in range(6):
        for z in range(6):
            count_num_ori = 0
            if my_number[i][j] == win_number_ori[z]:
                count_num_ori += 1
            count_one_ori += count_num_ori
        for z in range(7):
            count_num_bon = 0
            if my_number[i][j] == win_number_bon[z]:
                count_num_bon += 1
            count_one_bon += count_num_bon
    count_ori.append(count_one_ori)
    count_bon.append(count_one_bon)
cnt = tot = tot2 = tot3 = 0

one = two = thr = four = five = fail = 0

for i in range(5):
    if count_ori[i] == 6:
        one += 1
        continue
    elif count_bon[i] == 6:
        two += 1
    elif count_ori[i] == 5:
        thr += 1
    elif count_ori[i] == 4:
        four += 1
    elif count_ori[i] == 3:
        five += 1
    else:
        fail += 1
print("문제 3번 (일반버전) : 1등 {}개, 2등 {}개, 3등 {}개, 4등 {}개, 5등{} 개 탈락 {} 입니다.".format(one, two, thr, four, five, fail))

### 추가문제
### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?
### 로또 1게임은 1000원입니다.
number = 45
winning = 6
per = 1
for i in range(6):
    per = per*number/winning
    number -= 1
    winning -= 1
# print(per)
print("추가문제 : 투자해야 할 금액은 {} 입니다.".format(per*1000))
