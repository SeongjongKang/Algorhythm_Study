from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 1:
        return intervals
        # x부터 정렬 후 y 정렬
    intervals.sort(key = lambda x : (x[0], x[1]))
    result = []
    for i in intervals:
        if result and result[-1][1] >= i[0]:
            result[-1][1] = max(result[-1][1], i[1])
        else: result.append(i)
    return result
                

lst = [[1,4],[2,3]]

print(merge(lst))