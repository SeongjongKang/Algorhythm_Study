# 파이썬 내장함수 sort()를 사용하여 통과. 파이썬은 Tim Sort 방식으로 최악의 경우 시간복잡도가 nlogn 
# 최선일 경우 n으로 가장 빠른 정렬방법을 사용하므로 통과가 가능한듯하다.

import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()

for i in range(n):
    print(*lst[i])