
def riceCake(lst, req):
    if not lst:
        return 0
    lo = 1
    hi = max(lst)

    while lo <= hi:
        mid = (lo + hi)//2
        cut = 0
        for i in lst:
            if i > mid:
                cut += i-mid
        if cut >= req:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

lst = [19,15,10,17]
x = 6
print(riceCake(lst,x))