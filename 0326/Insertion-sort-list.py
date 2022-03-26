# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode(None)으로 지정하면 밑에 cur.val과 head.val을 비교할 때 NoneType과 int를 비교할 수 없다는 타입에러가 발생한다. 
        cur = root = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next
            if head and cur.val > head.val:
                cur = root
        return root.next
            
