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
INF = int(1e9)


def dijkstra_naive(graph, start):
    def get_smallest_node():
        min_value = INF
        idx = 0
        for i in range(1, N):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                idx = i
        return idx

    N = len(graph)
    visited = [False] * N
    dist = [INF] * N

    visited[start] = True
    dist[start] = 0

    for adj, d in graph[start]:
        dist[adj] = d

    # N개의 노드 중 첫 노드는 이미 방문했으므로,
    # N-1번 수행하면 된다.
    for _ in range(N - 1):
        # 가장 가깝고 방문 안한 녀석을 고르고,
        cur = get_smallest_node()
        visited[cur] = True
        # 최단거리를 비교, 수정한다.
        for adj, d in graph[cur]:
            cost = dist[cur] + d
            if cost < dist[adj]:
                dist[adj] = cost

    return dist