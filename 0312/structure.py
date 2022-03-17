
# 값이 들어갈 빈칸과 이동방향 즉 화살표를 만듦
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    #삽입
    def append(self, val):
        # self.head에 값이 존재 하지 않으면 아예 빈 연결 리스트이다. 그러므로 첫 번째에 값을 넣는다.
        # head는 제일 첫 번째 공간이다.
        if not self.head:
            self.head = ListNode(val, None)

            return
        else:
            node = self.head
            # 값이 없는 빈 칸까지 이동.
            while node.next:
                node = node.next

            # 마지막 node에 값을 넣는다, 이 노드의 next는 none이다.
            node.next = ListNode(val, None)

            return
    #삭제
    def pop(self, val):
        node = self.head
        if node.val == val:
            self.head = node.next
            del node
            return
        else:
            while node is not None:
                if node.val == val:
                    break
                prev = node
                node = node.next

            if node is None: return
            prev.next = node.next

            del node
            return






lst = [1,2,3]

l1 = LinkedList()
for e in lst:
    l1.append(e)

l1.pop(2)
print(l1)

