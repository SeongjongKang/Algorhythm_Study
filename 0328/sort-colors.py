from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        top, bottom = 0, len(nums)-1
        idx = 0
        while idx <= bottom:
            if nums[idx] < 1:
                nums[top], nums[idx] = nums[idx], nums[top]
                idx += 1
                top += 1
            elif nums[idx] > 1:
                nums[idx], nums[bottom] = nums[bottom], nums[idx]
                bottom -= 1
            else: # nums[idx] = 1 즉 중간 값일 때
                idx += 1

            

