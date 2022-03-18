#Counter를 이용
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = Counter(stones)
        answer = 0
          #Counter의 경우 빈 키의 경우 key error가 발생하지 않으므로 j가 count에 없을 경우를 생각 안해도 됨.
        for j in jewels:
            answer += count[j]
        return answer

##Hash Table을 이용
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         count = {}
#         for S in stones:
#             if S not in count:
#                 count[S] = 1
#             else:
#                 count[S] += 1
#         answer = 0
#         for j in jewels:
#             if j in count:
#                 answer += count[j]
#         return answer 
    
##파이썬다운 방식을 이용
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         return sum(S in jewels for S in stones)
