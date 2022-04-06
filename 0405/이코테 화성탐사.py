import sys
import heapq as hq

input = sys.stdin.readline
TC = int(input())
for i in range(TC):
    n = int(input())
    graph = []
    dist = [[] for _ in range(n)]
    for idx in range(n):
        dist[idx].append([11]*n)
    for j in range(n):
        lst = list(map(int, input().split()))
        graph.append(lst)
    h = []
    hq.heappush(h, (graph[0][0], 0, 0))
    while h:
        cost, x, y = hq.heappop(h)
        if dist[x][y] < cost:
            continue
        if x+1 <=n and y+1 <= n:
            a, b = x, y+1
            if cost+graph[a][b] < dist[a][b]:
                dist[a][b] = cost+graph[a][b]
                hq.heappush(h, (graph[a][b], a, b))
            a, b = x+1, y
            if cost+graph[a][b] < dist[a][b]:
                dist[a][b] = cost+graph[a][b]
                hq.heappush(h, (graph[a][b], a, b))
        else:
            if x+1 > n and y+1 <= n:
                a, b = x, y+1
            if x+1 <= n and y+1 > n:
                a, b = x+1, y
            if cost+graph[a][b] < dist[a][b]:
                dist[a][b] = cost+graph[a][b]
                hq.heappush(h, (graph[a][b], a, b))





    

