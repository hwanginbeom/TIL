# 11047 동전 문제
a, b = map(int, input().split())
count = 0
array = []

for i in range(a):
    c = int(input())
    array.append(c)

array.reverse()
for coin in array:
    count += b // coin
    b %= coin

print(count)

