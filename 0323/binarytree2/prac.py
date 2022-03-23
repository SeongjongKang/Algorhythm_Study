from collections import deque

class TreeNode:
    # self는 값이 존재해야 하지만 left와 right는 None일 수도 있다.
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    # lst[:mid]는 lst에서 mid > idx만 보여준다.
    node.left = sorted_array_to_bst(lst[:mid])
    # lst[mid+1:] lst에서 mid+1 <= idx만 보여준다(즉 mid보다 큰 idx만).
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node


def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst