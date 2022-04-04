import bisect

def findNumbers(lst, target):
    if not lst:
        return None
    bi1 = bisect.bisect_left(lst, target)
    if bi1 < len(lst) and lst[bi1] == target:
        bi2 = bisect.bisect_right(lst, target)
    return bi2 - bi1

l = [1,1,2,2,2,3,3,4]
t = 3

print(findNumbers(l, t))
