import sys

k, n = map(int, sys.stdin.readline().split())
lines = []
for i in range(k):
    lines.append(int(sys.stdin.readline().strip()))

lo = 1
hi = max(lines)
while lo <= hi:
    mid = lo + (hi-lo)//2
    std = 0
    for i in lines:
        std += i//mid
    if std >= n:
        lo = mid+1
    else:
        hi = mid-1

print(hi)