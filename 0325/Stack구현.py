
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.max_size = 10

    def push(self, val):
        if self.isFull():
            return "Already full"
        else:
            self.top = Node(val,self.top)
            self.size += 1

    def pop(self):
        if self.top is not None:
            node = self.top
            self.top = self.top.next
            self.size -= 1
            return node.val
        return "There is no data"
    
    def isEmpty(self):
        return self.top is None
    
    def isFull(self):
        return self.size == self.max_size

    def __str__(self):
        str_ = []
        node = self.top
        while node:
            str_.append(node.val)
            node = node.next
        str_.reverse()
        return str(str_)

# import copy
# 참조 값: 메모리에 저장되어 있는 객체의 주소 값
# 깊은복사 = 새로운 객체, 참조 생성 reversed(a)
# 얕은복사 = 객체의 참조 공유 a.reverse()
# deepcopy, [:], [::-1]
# deepcopy와 [:]의 차이점
# deepcopy는 n차원 배열들을 모두 깊은복사한다.
# [:]는 1차원 배열만을 깊은복사한다.


# k = [['a','b','c'],['d','e','f'],['g','h','i']]
# g = copy.deepcopy(k)
# g[0].append(1)[:]
# g.append([1,2,3])

# print(k,g)
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s)