# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        path_r=[]
        path_s=[]
        def visit(node,path):
            if not node:
                path.append('0')
                return
            visit(node.left,path)
            visit(node.right,path)
            path.append(str(node.val))
        
        visit(root, path_r)
        visit(subRoot, path_s)

        rs= ''.join(path_r)
        ss= ''.join(path_s)

        print(path_r, path_s)


        return ss in rs
