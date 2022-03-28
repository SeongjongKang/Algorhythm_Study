#파이썬 Recursion Error 발생으로 불가

import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, sys.stdin.readline().split())))

def QuickSort(lst, start, end):
    def partition(lst, start, end):
        pivot = lst[end][0]
        idx = start
        # while start < end:
        #     if lst[start][0] > pivot:
        #         start += 1
        #     elif lst[start][0] < pivot:
        #         lst[start], lst[idx] = lst[idx], lst[start]
        #         start += 1
        #         idx += 1
        #     else:
        #         if lst[start][1] > lst[end][1]:
        #             start += 1
        #         elif lst[start][1] < lst[end][1]:
        #             lst[start], lst[idx] = lst[idx], lst[start]
        #             start += 1
        #             idx += 1
        # lst[idx], lst[end] = lst[end], lst[idx]
        # return idx
        for j in range(start, end):
            if lst[j][0] < pivot:
                lst[j], lst[idx] = lst[idx], lst[j]
                idx += 1
            elif lst[j][0] == pivot:
                if lst[j][1] < lst[end][1]:
                    lst[j], lst[idx] = lst[idx], lst[j]
                    idx += 1
        lst[end], lst[idx] = lst[idx], lst[end]
        return idx

    if len(lst) == 0:
        return None
    if start >= end:
        return None

    mid = partition(lst, start, end)
    QuickSort(lst, mid+1, end)
    QuickSort(lst, start, mid-1)
    return lst

answer = QuickSort(lst, 0, n-1)
for i in range(n):
    print(*answer[i])
