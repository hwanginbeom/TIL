def solution(n, edge):
    answer = 0
    INF = 0
    # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
    visited = [False] * (n + 1)

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)

    graph = [ [INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b: graph[a][b] = 0

    for i in range(len(edge)):  #
        a, b = edge[i]
        graph[a][b] = 1
        graph[b][a] = 1

    def get_smallest_node():
        min_value = INF
        index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
        for i in range(1, n + 1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
            index = i
        return index

    def dijjkstra(start):
        # 시작 노드에 대해서 초기화
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1]
        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        for i in range(n - 1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    print(graph)

    return answer

n =  6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(n, edge)