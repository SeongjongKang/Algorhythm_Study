# 람다를 사용하여 y축부터 정렬
import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    print(*lst[i])