# 1956
import sys
#n은 마을 m은 도로
n,m = map(int,sys.stdin.readline().split())
inf = 100000000
s = [[inf] * n for i in range(m)]
for i in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    s[a-1][b-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if s[i][j] > s[i][k] + s[k][j]:
                s[i][j] = s[i][k] + s[k][j]
result = inf
for i in range(n):
    result = min(result, s[i][i])
if result == inf:
    print(-1)
else:
    print(result)
