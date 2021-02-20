'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지
조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시
통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는
사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는
프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서
세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다.
(1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다.
(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''

import sys
import heapq

input = sys.stdin.readline



# 노드의 개수, 간선의 개수를 입력받기
node, route = map(int, input().split())
# node, route = 4,6

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
distance = [int(1e9)] * (node + 1)
distances = []
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[]for i in range(node + 1)]
# graph = [[], [(2, 3), (3, 5), (4, 4)], [(1, 3), (3, 3), (4, 5)], [(2, 3), (4, 1), (1, 5)], [(3, 1), (2, 5), (1, 4)]]

# 모든 간선 정보를 입력 받기
for _ in range(route):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
one_node, two_node = map(int, input().split())
# one_node, two_node = 2,3

def dijkstra(distance,start):
    q = []
    distance = distance[:] # 이부분이 핵심이다. 이렇게 넣어줘야 각각의 distance를 만들어 줄수있다.
    # 시작 노드에 대해서 초기화
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


c1 = dijkstra(distance, 1)
c2 = dijkstra(distance, one_node)
c3 = dijkstra(distance, two_node)
ans = min((c1[one_node]+c2[two_node]+c3[node]), (c1[two_node]+c3[one_node]+c2[node]))
print(-1 if ans >= INF or ans < 0 else ans)
