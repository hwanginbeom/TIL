"""
# 깊이 우선 탐색

Depth First Search, DFS라고 불리며, 구현하기 쉬운 알고리즘 중 하나이다. 이름 그대로, 방문한 정점으로부터 깊게 들어가며 쭉 탐색한 후, 되돌아 나오다가 아직 탐색하지 않은 노드를 탐색하는 방식을 사용한다.

알고리즘의 실행과정을 설명하면 다음과 같다.

첫 정점을 방문한다.
인접한 정점 중 아직 방문하지 않은 정점을 방문한다(한 길로 쭉 파고 들어간다).
더 이상 들어갈 길이 없을 때(인접한 모든 정점이 이미 방문한 정점일 때), 방문하지 않은 인접한 정점을 찾을 때까지 들어간 길을 돌아나온다.
위 과정을 반복한다.
여기서 DFS를 구현하는 함수의 모양은 다음과 같다. 단,그래프는 인접리스트를 활용했다고 가정한다.
"""

visited = dict(zip([v for v G], [False for _ in G]))

def dfs(v):
    for i in G[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)



"""
#너비우선탐색
Breadth First Search, BFS라고 불린다. 이름 그대로, 넓게 퍼져가며 정점을 방문한다.

알고리즘의 실행과정은 다음과 같다.

첫 정점을 방문한다.
아직 방문하지 않은 인접한 정점들을 큐에 넣는다.
큐에 있는 정점들을 순서대로 방문한다.
큐에 있는 정점에 대해 인접하면서 아직 방문하지 않은 정점들로 새로운 큐를 구성한다.
위 과정을 반복한다.
예제(그림)의 경우 방문 순서는 1, 2, 5, 6, 3, 4, 7, 8, 9 이다.
"""

visited = dict(zip([v for v in G], [False for _ in G])) # 방문 여부를 체크하는 배열

def bfs(v): # 정점 v부터 탐색 시작
    visited[v] = True
    queue = [v]
    while queue:
        now = queue.pop(0)
        for i in G[now]: # 현재 선택한 정점의 모든 자식 정점을 방문.
            if not visited[i]:
                visited[i] = True
                queue.append(i)