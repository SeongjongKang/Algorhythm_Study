import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

lo = 1
hi = max(trees)

while lo <= hi:
    mid = (lo+hi)//2
    tree = 0
    for i in trees:
        if i - mid < 0 :
            continue
        tree += i-mid
    if tree >= m:
        lo = mid + 1
    else:
        hi = mid - 1
print(hi)


        
