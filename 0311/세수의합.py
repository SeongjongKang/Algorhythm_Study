from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for k in range(i+1, len(nums)-1):
            if k>i+1 and nums[k] == nums[k-1]:
                continue
            for j in range(k+1, len(nums)):
                if j>k+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i]+nums[k]+nums[j] == 0:
                    results.append([nums[i], nums[k], nums[j]])
    return results

num = [-1, -2, -3, 0, 1, 2, 3]



def threeSum_twoPoint(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i]+nums[left]+nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results
print(threeSum_twoPoint(num))