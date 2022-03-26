from typing import List

class Solution:
    def largestNumber(nums: List[int]) -> str:
        # index를 1부터 n-1까지 본다
        for idx in range(1,len(nums)):
            val = nums[idx]
            cmp = idx - 1
            # index가 idx인 위치의 값과 idx-1 인 바로 전 위치의 값을 문자로바꿔 a+b, b+a를 비교해서 index = 0 위치의 값까지 비교해 나간다.
            while cmp >= 0 and str(val)+str(nums[cmp]) > str(nums[cmp])+str(val):
                # 만약 val = 4, nums[cmp] =  45의 비교라면 454 > 445이므로 값을 바꿔준다.
                nums[cmp], nums[cmp+1] = nums[cmp+1], nums[cmp]
                # index가 0인 위치까지 비교하기 위함
                cmp -= 1
        # nums = [0,0]인 경우 str로만 반환하면 00이 되므로 join한 string들을 정수로 한번 변환 후 다시 문자열로 변환했다.
        return str(int("".join(map(str, nums))))



n = [3,30,34,5,9]
print(Solution.largestNumber(n))