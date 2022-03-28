from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
        # 연결리스트를 리스트로 표현 후 내장함수를 사용하여 정렬.
        lst.sort()
        # 정렬한 리스트를 다시 연결리스트로 변환.
        p = head
        for i in lst:
            p.val = i
            p = p.next
        return head
