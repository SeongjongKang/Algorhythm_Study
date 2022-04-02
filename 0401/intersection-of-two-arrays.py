import bisect
from typing import List

# 아무래도 sort의 시간 복잡도가 Big0 nlogn이고, bisect로 교집합을 찾는 시간 복잡도 Big0 nlogn과 같아
# 길이가 더 작은 걸 sort하면 빠를 거라 생각해 조건을 추가했는데 3회 평균 약 50ms로 조금 더 빨랐다.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        if not nums1 or not nums2:
            return answer
        if len(nums1) > len(nums2):
            nums2.sort()
            for i in nums1:
                bi = bisect.bisect_left(nums2, i)
                if len(nums2) > bi and nums2[bi] == i:
                    answer.add(i)
        else:
            nums1.sort()
            for i in nums2:
                bi = bisect.bisect_left(nums1, i)
                if len(nums1) > bi and nums1[bi] == i:
                    answer.add(i)                
        return answer


# 3회평균 60ms
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        if not nums1 or not nums2:
            return answer
        nums2.sort()
        for n1 in nums1:
            idx = bisect.bisect_left(nums2, n1)
            if len(nums2) > idx and n1 == nums2[idx]:
                answer.add(n1)

        return list(answer)