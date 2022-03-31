import sys
# import heapq
n = int(sys.stdin.readline())

answer = []
# for _ in range(n):
#     heapq.heappush(answer, int(sys.stdin.readline().strip()))

# for _ in range(n):
#     print(heapq.heappop(answer))
for _ in range(n):
    answer.append(int(sys.stdin.readline().strip()))

answer.sort()

for i in range(n):
    print(answer[i])