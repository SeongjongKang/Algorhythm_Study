n = int(input())
m = int(input())
visited = []
graph = {}

for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
        graph[b].append(a)
    else:
        graph[a] = [b]
        graph[b] = [a]

def VirusDFS(start, graph):
    stack = [start]

    while stack:
        a = stack.pop()
        visited.append(a)
        for i in graph[a]:
            if i not in visited and i not in stack:
                stack.append(i)

VirusDFS(1,graph)
print(len(visited)-1)
