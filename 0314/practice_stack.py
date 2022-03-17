
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.value

    def is_empty(self):

        return self.top is None
