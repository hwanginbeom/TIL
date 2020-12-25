# 15897 - 잘못 구현한 에라토스테네스의 체
# import math
#
# n = int(input())
# m = n
# # array = [True for i in range(n + 1)]
# number  = 0
# print(math.sqrt(n))
# for i in range(1,int(math.sqrt(n) + 1)):
#     number   += (n / i + 1) * (i - (n / ((n / i) + 1)))

# 12
# 6
# 4
# 3
# 3
# 2
# 2
# 2
# 2
# 2
# 2
# 1
n = int(input())
number  = 0

for i in range(1,n+1):
    for j in range(1, n+1, i):
        # array[j] += 1
        number += 1
print(number)
