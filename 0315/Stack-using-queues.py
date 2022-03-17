import collections

class MyStack:
    # deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
    # deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
    # deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
    # deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
    # deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
    # deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
    # deque.remove(item): item을 데크에서 찾아 삭제한다.
    # deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
    def __init__(self):
        self.deq = collections.deque()
    def push(self, x: int):
        self.deq.append(x)
        for i in range(len(self.deq)-1):
            self.deq.append(self.deq.popleft())
    # def push(self, x: int):
    #     self.deq.append(x)
    #     for i in range(len(self.deq)-1):
    #         self.deq.rotate(-1)

    def pop(self):
        return self.deq.popleft()
    def top(self):
        return self.deq[0]
    def empty(self):
        return len(self.deq) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
