#2217 로프 ( sort)
import sys
input = sys.stdin.readline

N = int(input())
result = []
for i in range(N):
    result.append(int(input()))
result.sort(reverse=True)

max_value = 0
for i in range(len(result)):
    temp = result[i] * (i+1)
    if temp > max_value:
        max_value = temp
print(max_value)