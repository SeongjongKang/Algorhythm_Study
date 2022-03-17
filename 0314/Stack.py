class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    # 새로운 top을 만들어 값을 넣고 기존의 top에 연결
    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None
        # node에 삭제할 top을 넣고, 기존 top의 연결을 끊고, 기존 top의 next가 새로운 top이 된다. 그리고 node 즉 기존 top의 value를 반환한다.
        node = self.top
        self.top = self.top.next

        return node.item

    def is_empty(self):
        return self.top is None