# 1149 RGB 거리
# import sys
# home = int(input())
# print(home)
# array = []
# # d = [0] * 100
# # d[1] =
# # d[2] =
# for i in range(home):
#     data = list(map(int, sys.stdin.readline().split()))
#     array.append(data)

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(p[n - 1][0])
print(p[n - 1][1])
print(p[n - 1][2])
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))



# 다른 풀이

