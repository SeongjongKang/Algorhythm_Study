
class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        self.top = Node(value,self.top)

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = self.top.next
        return node.value

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None

    def push(self,value):
        if not self.front:
            self.front = Node(value,None)

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value,None)

    def pop(self):
        if not self.front:
            return None
        node = self.front
        self.front = self.front.next

        return node.value

    def is_empty(self):
        return self.front is None

