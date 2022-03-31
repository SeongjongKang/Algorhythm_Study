import heapq 
import sys

user = []
n = int(sys.stdin.readline())
for _ in range(n):
    heapq.heappush(user, list(sys.stdin.readline().split()))

for _ in range(n):
    print(*heapq.heappop(user))
