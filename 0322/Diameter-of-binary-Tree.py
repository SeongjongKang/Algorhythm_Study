# 이진트리가 주어졌다면.

class solution:
    longest: int = 0 
    # 중첩함수(nested function)는 자신이 속한 함수 안에서만 역할을 하며, 부모함수 밖에서는 인식이 안된다.
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)
            return max(left, right) + 1

        dfs(root)

        return self.longest