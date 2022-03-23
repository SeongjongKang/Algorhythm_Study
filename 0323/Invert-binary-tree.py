# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right
        
def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return
        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2*idx + 1)
        parent.right = make_tree_by(lst, 2*idx + 2)
    return parent

# Queue를 이용하여 lst 정렬
def make_lst_by(root):
    if root is None:
        return []
    lst = []
    q = deque([root])
    while q is not None:
        node = q.popleft()
        lst.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return lst

# 파이썬 다운 방식
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is not None:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None

# 반복구조 BFS
def invertTree(self, root: TreeNode) -> TreeNode:
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)
    return root
# 반복구조 DFS: 오른쪽으로 탐색
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = list([root])

    while stack:
        node = stack.pop()
        if node:
            # 노드를 바꾼 후 스택에 넣는다
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)
    return root
# 반복구조로 DFS 후위 순위: 왼쪽으로 탐색
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = list([root])

    while stack:
        node = stack.pop()
        if node:
            # 스택에 넣은 후 노드를 바꾼다.
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left
    return root
    


