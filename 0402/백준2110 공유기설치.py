import sys

n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline().strip()))

def routerSetting(lst, c):
    lst.sort()
    lo = 1
    hi =  lst[-1]-lst[0]
    
    
    while lo <= hi:
        mid = lo + (hi-lo)//2
        cnt = 1
        cur = lst[0]
        for i in range(1,len(lst)):
            if lst[i] - cur >= mid:
                cur = lst[i]
                cnt += 1
        
        if cnt >= c:
            lo = mid + 1
            global answer
            answer = mid
        else:
            hi = mid - 1
    return answer
print(routerSetting(house, c))