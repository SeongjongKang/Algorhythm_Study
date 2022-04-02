from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums)-1
        while start < end:
            mid = start+(end-start)//2
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        pivot = start
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start+(end-start)//2
            mid_pivot = (mid+pivot)%len(nums)
            if nums[mid_pivot] > target:
                end = mid-1
            elif nums[mid_pivot] < target:
                start = mid+1
            else:
                return mid_pivot
        return -1



