# 4386번 - 별자리만들기
import sys
import math
import heapq

n = int(sys.stdin.readline())
s_location = []  # 별위치저장
G = [[] for _ in range(n)]  # 별들간의 거리
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    s_location.append([x, y])

# print(s_location)
for i in range(n - 1):
    for j in range(i, n):
        # 각 별간의 거리 계산
        dis = round(math.sqrt((s_location[i][0] - s_location[j][0]) ** 2 + (s_location[i][1] - s_location[j][1]) ** 2),
                    2)
        if i == j:  # 자신으로 가는 거리는 계산하지않음
            continue
        # 양방향 저장
        G[i].append([dis, j])
        G[j].append([dis, i])

# 프림 알고리즘을 사용하기 위해 최소힙사용
q = []
heapq.heappush(q, [0, 0])

mst_value = 0
check = [0 for _ in range(n)]  # 이어진별 체크
while q:
    dis, end = heapq.heappop(q)
    if check[end] == 1:  # 이미 이어져 있는 별이라면
        continue
    mst_value += dis  # 최소거리 갱신
    check[end] = 1  # 이어짐 체크
    for dis, end in G[end]:  # 해당 별에서 이어진 모든 별 점검
        heapq.heappush(q, [dis, end])

print(mst_value)

