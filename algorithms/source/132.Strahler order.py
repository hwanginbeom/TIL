import sys
from collections import deque

def topology_sort(test_case):
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용 # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, m + 1):
        if indegree[i] == 0: q.append(i) # 큐가 빌 때까지 반복
    # print(test_case,max(indegree))
    count_list=[]
    while q: # 큐에서 원소 꺼내기
        now = q.popleft()
        count = 1
        result.append(now) # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            count+=1
            if indegree[i] == 0:
                q.append(i)
                count_list.append(count)
    print(test_case,max(count_list))
    # for i in result:
        # print(i, end=' ')
    # print()


test_case = int(sys.stdin.readline())

for i in range(1,test_case+1):
    k, m, p = map(int, sys.stdin.readline().split())
    indegree = [0] * (m + 1)

    graph = [[] for i in range(m + 1)]

    for _ in range(p):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)  # 정점 A에서 B로 이동 가능 # 진입 차수를 1증가
        indegree[b] += 1
        # print()
    topology_sort(i)





# print(test_case)