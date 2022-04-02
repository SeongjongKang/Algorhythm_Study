from typing import List
import bisect
# Two-pointer로 풀이
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: return [left+1, right+1]
# bisect로 풀이
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx,val in enumerate(numbers):
            x = target - val
            # numbers라는 array에서 x를 찾는 데 idx+1 인덱스부터 찾는다.
            bi = bisect.bisect_left(numbers,x,idx+1)
            if len(numbers) > bi and numbers[bi] == x:
                return idx+1, bi+1