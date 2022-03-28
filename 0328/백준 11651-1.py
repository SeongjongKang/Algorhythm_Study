# x, y 자리를 바꿔 lst를 만들어 정렬. 프린트 시 x, y의 자리를 바꾸어 프린트. 시간 528ms
import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([y, x])

lst.sort()

for i in range(n):
    print(lst[i][1], lst[i][0])
