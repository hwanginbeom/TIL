# 10217번
input = __import__('sys').stdin.readline
Max = float('INF')
# 테스트 케이스
for __ in range(int(input())):
    # n - 공항의 수 / m - 총 지원비용 / k 티켓정보
    n, m, k=map(int, input().split())
    D = [[] for _ in range(n+1)]
    for i in range(k):
        #u=티켓의 출발공항 , v- 도착공항, c-비용,d-소요시간
        u, v, c, d=map(int, input().split())
        # 출발공항에서 도착공항/비용/소요시간
        D[u].append((v, c, d))
    S=[[Max]*(m+1) for _ in range(n+1)]
    S[1][0] = 0
    for e in range(m+1):
        for x in range(1, n+1):
            if S[x][e] == Max: continue
            t = S[x][e]
            for nx, ne, nt in D[x]:
                if ne+e > m: continue
                S[nx][ne+e] = min(S[nx][ne+e], t+nt)
    k = min(S[n])
    print([k, 'Poor KCM'][k == Max])