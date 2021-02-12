count = 0
def dfs(graph, v, visited):
    visited[v] = True
    global count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

computer = int(input())
connect_num = int(input())
node = []

for i in range(0,computer+1):
    node.append([])
for i in range(0,connect_num):
    node_num, connect = list(map(int, input().split()))
    node[node_num].append(connect)
    node[connect].append(node_num)

visited = [False] * (computer+1)
dfs(node, 1, visited)
count = count-1
print(count)