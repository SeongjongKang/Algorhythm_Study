# import sys

# from min_cost.dijkstra import dijkstra_naive, dijkstra_pq

# with open('testcase1.txt') as f:
#     sys.stdin = f
#     input = sys.stdin.readline
#     n, m = map(int, input().split())
#     start = int(input())
#     graph = [[] for _ in range(n + 1)]

#     for _ in range(m):
#         a, b, c = map(int, input().split())
#         graph[a].append((b, c))

# assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]
# assert dijkstra_pq(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]

import heapq
INF = int(1e9)

def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist


def dijkstra_hq(graph, start):
    N = len(graph)
    distance = [INF]*N
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for adj, d in graph[now]:
            cost = dist + d
            if cost < distance[adj]:
                distance[adj] = cost
                heapq.heappush(q, (cost, adj))
    return distance


def dijkstra_heapq(graph, start):
    q = []
    n = len(graph)
    D = [INF]*n
    D[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        acc, now = heapq.heappop(q)

        if D[now] < acc:
            continue

        for adj, d in graph[now]:
            cost = acc + d
            if D[adj] > cost:
                D[adj] = cost
                heapq.heappush(q, (cost, adj))

    return D
