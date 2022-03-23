class TreeNode:
    # self는 값이 존재해야 하지만 left와 right는 None일 수도 있다.
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right