# 삽입정렬로 만들어 봤지만 시간초과

import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

def insertionSort(lst, n):
    for i in range(1, n):
        val1 = lst[i][0]
        val2 = lst[i][1]
        cmp = i - 1
        while cmp >= 0 and lst[cmp][0] >= val1:
            if lst[cmp][0] == val1 and lst[cmp][1] < val2:
                break
            lst[cmp+1] = lst[cmp]
            cmp -= 1
        lst[cmp+1] = [val1, val2]
    return lst
answer = insertionSort(lst, n)
for i in range(n):
    print(*answer[i])

