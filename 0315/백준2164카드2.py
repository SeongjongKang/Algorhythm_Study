N = 6

class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class solution:
    def __init__(self):
        self.front = None

    def Queue_linked_list(self):
        for i in range(1, N+1):
            if not self.front:
                self.front = Node(i,None)

            node = self.front
            while self.front:
                node = node.next
            node.next = Node(i,None)

    def cards2(self):
        while self.front.next:
            if self.front is None:
                return None

            self.front = self.front.next

            node = self.front
            while self.front:
                node = node.next
            node.next = self.front
            self.front = self.front.next

        return self.front



