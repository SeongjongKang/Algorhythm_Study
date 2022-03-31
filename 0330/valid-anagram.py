# sort()같은 경우는 문자열 정렬 시 오류가 발생한다.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

