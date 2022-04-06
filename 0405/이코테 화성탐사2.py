import sys
import heapq as hq

input = sys.stdin.readline
TC = int(input())

def mars(graph):
    n = len(graph)
    dist = [[11]*n for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    hq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]
    while q:
        acc, x, y = hq.heappop(q)

        if acc > dist[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = acc + graph[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    hq.heappush(q, (cost, nx, ny))
    return dist[n-1][n-1]

for i in range(TC):
    n = int(input())
    graph = []
    for j in range(n):
        graph.append(list(map(int, input().split())))
    print(mars(graph))