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
            if abs(depth(node.left) - depth(node.right))<=1:
                print(depth(node.left),depth(node.right))

                return 1+ max(depth(node.left),depth(node.right))
            else:
                print(node)
                self.binary=False
                return 1+ max(depth(node.left),depth(node.right))
        
        depth(root)
        return self.binary