class MyCircularQueue:

    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.size = k
        self.queue = [None] * k

    def enQueue(self, value: int) -> bool:
        if self.queue[self.rear] is None:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            return True
        else:
            return False
    # not self.queue[self.front] 는 self.queue[self.front] = 0과 같은 뜻
    def deQueue(self) -> bool:
        if self.queue[self.front] is None:
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        return -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.queue[self.rear - 1] is None else self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.queue[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

