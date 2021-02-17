from collections import deque


n = int(input())
score = deque()

dp = [0] * (n + 1)

for i in range(n):
    score.appendleft(int(input()))

if n == 1:
    print(score[0])
elif n == 2:
    print(score[0]+score[1])
elif n == 3:
    print(max(score[0]+score[2] ,score[0]+score[1] ))
else:
    dp[0]=score[0]
    dp[1]=score[0]+score[1]
    dp[2]=max(score[0]+score[2] ,score[0]+score[1])

    for i in range(3,n-1):
        dp[i] = max(dp[i-1]+score[i+1],dp[i-2]+score[i]+score[i+1])
    print(dp[n-2])
    print(dp)