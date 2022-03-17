
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.front = None

    def push(self,value):
        # 아무 값도 없으면 front라는 노드를 만들어 값과 next = None으로 넣어줌.
        if not self.front:
            self.front = Node(value,None)

        node = self.front
        # node의 가장 끝으로 가서
        while node.next:
            node = node.next
        # node.next에 새로운 노드를 연결
        node.next = Node(value,None)

    def pop(self):
        if not self.front:
            return None
        node = self.front
        # self.front를 패싱
        self.front = self.front.next
        return node.value

    def is_empty(self):
        return self.front is None



