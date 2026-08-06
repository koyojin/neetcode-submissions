# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.binary=True
        def depth(node):

            if not node:
                print('none')
                return 0
            l=depth(node.left)
            r=depth(node.right)
            if abs(l-r)<=1:
                return 1+ max(l,r)
            else:
                print(node)
                self.binary=False
                return 1+ max(l,r)
        
        depth(root)
        return self.binary