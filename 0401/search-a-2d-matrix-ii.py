import bisect
from typing import List
# 이진탐색
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        lm = len(matrix)
        ln = len(matrix[0])
        for i in range(lm):
            if matrix[lm-1-i][0] <= target:
                bi = bisect.bisect_left(matrix[lm-1-i], target)
                if ln > bi and matrix[lm-1-i][bi] == target:
                    return True
        return False


# 이진탐색보다 느리다.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) -1 
        while row <= len(matrix)-1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False