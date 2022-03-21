from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
# 밑에로 하면 왜 안될까?
# graph = [list(input()) for _ in range(n)]
answer = []

def BFS(graph,x,y):
    n = len(graph)
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1
    
    while q:
        i, j = q.popleft()
        for _ in range(4):
            X = i + dx[_]
            Y = j + dy[_]
            if X < 0 or X >= n or Y < 0 or Y >= n:
                continue
            if graph[X][Y] == 1:
                graph[X][Y] = 0
                q.append((X,Y))
                count += 1
    return count

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            answer.append(BFS(graph,x,y))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])

