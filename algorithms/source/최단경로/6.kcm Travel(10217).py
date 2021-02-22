"""
문제
각고의 노력 끝에 찬민이는 2014 Google Code Jam World Finals에 진출하게 되었다. 구글에서 온 초대장을 받고 기뻐했던 것도 잠시, 찬찬히 읽어보던 찬민이는 중요한 사실을 알아차렸다. 최근의 대세에 힘입어 구글 역시 대기업답게 비용 감축에 열을 내고 있었던 것이다.

초대장 내용에 의하면 구글은 찬민에게 최대 M원까지의 비용만을 여행비로써 부담해주겠다고 한다. 인천에서 LA행 직항 한 번 끊어주는게 그렇게 힘드냐고 따지고도 싶었지만, 다가올 결승 대회를 생각하면 대회 외적인 곳에 마음을 쓰고 싶지 않은 것 또한 사실이었다. 그래서 찬민은 인천에서 LA까지 M원 이하로 사용하면서 도착할 수 있는 가장 빠른 길을 차선책으로 택하기로 하였다.

각 공항들간 티켓가격과 이동시간이 주어질 때, 찬민이 인천에서 LA로 갈 수 있는 가장 빠른 길을 찾아 찬민의 대회 참가를 도와주자.

입력
입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 줄에는 공항의 수 N (2 ≤ N ≤ 100), 총 지원비용 M (0 ≤ M ≤ 10,000), 티켓정보의 수 K (0 ≤ K ≤ 10,000)가 공백으로 구분되어 주어진다. 이어서 K개의 줄에 걸쳐 각 티켓의 출발공항 u, 도착공항 v (1 ≤ u, v ≤ N, u ≠ v), 비용 c (1 ≤ c ≤ M, 정수), 그리고 소요시간 d (1 ≤ d ≤ 1,000) 가 공백으로 구분되어 주어진다. 인천은 언제나 1번 도시이고, LA는 언제나 N번 도시이다

출력
각 테스트 케이스당 한 줄에 찬민이 LA에 도착하는 데 걸리는 가장 짧은 소요시간을 출력한다.

만약, LA에 도착할 수 없는 경우 "Poor KCM"을 출력한다.
"""


import sys
import heapq
from collections import deque

#

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
input = sys.stdin.readline

def dijkstra(start):
    q = deque()
    # INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
    distance = [[INF]*(m+1) for _ in range(n+1)]

    # distance = distance[:] # 이부분이 핵심이다. 이렇게 넣어줘야 각각의 distance를 만들어 줄수있다.
    # 시작 노드에 대해서 초기화
    # print(distance)
    # heapq.heappush(q,[0, 0, start])
    q.append((0, 0, 1))
    distance[start][0] = 0
    while q:
        # dist, cost, now = heapq.heappop(q)
        dist, cost, now = q.popleft()
        if distance[now][cost] != dist:
            continue
        for v, c, d in graph[now]:
            dist_sum = dist + d
            cost_sum = cost + c
            if cost_sum > m:
                continue
            if dist_sum < distance[v][cost_sum]:
                distance[v][cost_sum] = dist_sum
                # heapq.heappush(q, (dist_sum, cost_sum, v))
                q.append((dist_sum, cost_sum, v))
    ans = min(distance[n])
    return ans


test_case = int(input())

for i in range(test_case):
    # 공항의 개수, 지원비용, 티겟 정보의개수를 입력받기
    n, m, k = map(int, input().split())

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[]for i in range(n + 1)]

    # 모든 티켓 정보를 입력 받기
    for _ in range(k):
        u, v, c, d = map(int, input().split()) # u 출발 ,v 도착, c 비용 d 시간
        graph[u].append([v,c,d])


    ans = dijkstra(1)
    print(ans if ans != INF else "Poor KCM")