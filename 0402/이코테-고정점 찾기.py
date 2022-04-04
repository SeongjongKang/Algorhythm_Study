
def fixedPoint(lst):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = left+(right-left)//2
        if lst[mid] < mid:
            left = mid+1
        elif lst[mid] > mid:
            right = mid-1
        else: return mid
    return -1

l = [-1,1,3,5,7]

print(fixedPoint(l))


