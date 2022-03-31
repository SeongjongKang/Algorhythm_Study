import sys

user = []
n = int(sys.stdin.readline())
for _ in range(n):
    user.append(list(sys.stdin.readline().split()))

user.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(*user[i])