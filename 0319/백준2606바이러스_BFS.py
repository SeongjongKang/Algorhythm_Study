from collections import deque

n = int(input())
m = int(input())
visited = []
graph = {}

for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def VirusBFS(start, graph):
    visited.append(start)
    q = deque([start])
    while q:
        node = q.popleft()
        for i in graph[node]:
            if i not in visited:
                q.append(i)
                visited.append(i)

VirusBFS(1, graph)
print(len(visited)-1)
print(graph)
