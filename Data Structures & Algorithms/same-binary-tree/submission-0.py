# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        path_p=[]
        path_q=[]
        def visit(node, path):
            if not node:
                path.append(None)
                return
            path.append(node.val)
            visit(node.left, path)
            visit(node.right, path)

        visit(p, path_p)
        visit(q, path_q)

        return path_p==path_q
            