# 1541번 문제 - 잃어버린 괄호 (그리디)
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
    print(num)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)