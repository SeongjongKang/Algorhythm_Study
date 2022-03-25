class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    
class Queue:
    # self.IN은 가장 최근에 들어온 데이터
    # self.OUT은 가장 예전에 들어와 가장 먼저 pop될 데이터
    def __init__(self):
        self.IN = None
        self.OUT = None
        self.size = 0
        self.Max_size = 20

    def push(self,val):
        if self.isFull():
            return print("Already full")
        if self.isEmpty():
            self.IN = Node(val)
            self.OUT = self.IN
        else:
            self.IN.next = Node(val)
            self.IN = self.IN.next
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return print("There is no data to be deleted")
        node = self.OUT
        self.OUT = node.next
        self.size -= 1
        return node.val

    def isFull(self):
        return self.size == self.Max_size
    
    def isEmpty(self):
        return self.size == 0
    
    def QueueSize(self):
        return self.size
    
    def peek(self):
        if not self.isEmpty():
            return self.OUT.val 
        return print("There is no data")
        
    def __str__(self) -> str:
        str_ = []
        node = self.OUT
        while node:
            str_.append(node.val)
            node = node.next
        return str(str_)


q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.pop()
a = q.peek()
print(q, a)
    