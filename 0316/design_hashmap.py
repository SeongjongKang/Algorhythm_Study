# 개별 체이닝 방식의 해시맵 -> 연결리스트 노드 필요
import collections

class ListNode:
    def __init__(self, key = None, value = None) -> None:
        self.key = key
        self.value = value
        self.next = None    


class MyHashMap:
    def __init__(self):
        self.size = 1000
        # defaultdict: 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성, 에러 발생 없음.
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # index 즉 키 값으로 조회하지 않고 value 값으로 조회하는 이유는 defaultdict이 없는 키 조회시 그 키와 빈 ListNode를 생성하기 때문이다.
        if self.table[index].value is None:
            # 해당 index에 아무것도 없을 경우 새로 Node를 만들고 반환
            self.table[index] = ListNode(key, value)
            return
        p = self.table[index]
        while p:
            # key가 있다면 새로 업데이트하고 반환
            if p.key == key:
                p.value = value
                return
            # key를 가진 노드를 찾지 못하고 가장 오른쪽까지 왔을 때, 루프를 빠져나간다.
            if p.next is None:
                break
            # 연결리스트 오른쪽으로 계속 이동하다가 next가 None이면 멈춤 즉 가장 오른쪽으로 이동
            p = p.next
        # 루프를 빠져나온 후 새 노드 생성
        p.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % self.size
        # 해당 key값으로 저장된 값이 None일 경우 -1반환
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        # index의 첫 번째 노드일 때 삭제
        p = self.table[index]
        if p.key == key:
            # 애당초 self.table은 defaultdict이기에 빈 노드를 생성하므로 ListNode()를 할당했다.
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # prev는 바로 이전 노드, p는 현재 노드로 정하여 key값을 가진 노드를 찾고, 찾았다면 현재 노드를 제외시킨다.
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

        
