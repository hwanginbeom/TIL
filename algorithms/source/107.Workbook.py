# 1786번 - 문제집

import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)]

q = []
# 문제 순서
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    inDegree[b] += 1

# 진입차수가 0이면 큐에 넣기
for i in range(1, N + 1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

# 위상정렬
result = []
while q:
    a = heapq.heappop(q)  # 최소힙 사용
    result.append(a)
    for i in tree[a]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)

print(*result)

