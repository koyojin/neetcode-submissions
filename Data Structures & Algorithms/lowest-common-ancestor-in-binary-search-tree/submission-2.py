# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mem=[]
        lo, hi = min(p.val, q.val), max(p.val, q.val)

        def visit(node,p,q):
            if not node:
                return
            visit(node.right,p,q)
            visit(node.left,p,q)
            if lo<= node.val  and hi>=node.val:
                mem.append(node)

        visit(root,p,q)
        print(mem)
        return mem[-1]            
        