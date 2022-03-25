class heap:
    def __init__(self) -> None:
        self.item = [None]
    
    def __len__(self):
        return len(self)-1

    def insert(self, val):
        self.item.append(val)
        self.percolate_up()

    def extract(self):
        if len(self) < 1:
            return None
        root = self.item[1]  
        self.item[1] = self.item[-1]
        self.pop()
        self.percolate_down(1)
        return root

    def percolate_up(self):
        cur = len(self)
        parent = cur//2
        while parent > 0:
            if self.item[cur] > self.item[parent]:
                self.item[parent], self.item[cur] = self.item[cur], self.item[parent]
                cur = parent
                parent = cur//2

    def percolate_down(self, idx):
        biggest = idx
        left = 2*biggest
        right = 2*biggest + 1

        if left <= len(self) and self.item[left] > self.item[biggest]:
            biggest = left
        if right <= len(self) and self.item[right] > self.item[biggest]:
            biggest = right
        if biggest != idx:
            self.item[biggest], self.item[idx] = self.item[idx], self.item[biggest]
            self.percolate_down(biggest)
        



