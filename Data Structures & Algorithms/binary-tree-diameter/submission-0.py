# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        
        def depth(node):
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            self.best = max(self.best, l + r)  # 이 노드를 지나는 지름 후보
            return 1 + max(l, r)
        
        depth(root)
        return self.best