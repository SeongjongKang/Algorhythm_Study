import sys
n = int(sys.stdin.readline())
province = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
s = sum(province)
if s < m:
    hi = max(province)
else:
    lo = 1
    hi = max(province)
    while lo <= hi:
        limit = (lo+hi)//2
        sum = 0
        for i in province:
            if i <= limit:
                sum += i
            else: 
                sum += limit
        
        if sum <= m:
            lo = limit+1
        else:
            hi = limit-1
print(hi)

    