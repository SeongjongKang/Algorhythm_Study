import heapq as hq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dis = x**2 + y**2
            hq.heappush(heap,(dis, x, y))
        
        answer = []
        for _ in range(k):
            (d, a, b) = hq.heappop(heap)
            answer.append([a, b])
        return answer
