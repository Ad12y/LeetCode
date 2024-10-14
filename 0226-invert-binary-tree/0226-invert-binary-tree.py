# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(ptr):
            if not ptr:
                return 
            else:
                ptr.left, ptr.right = ptr.right, ptr.left
                recur(ptr.left)
                recur(ptr.right)
            return ptr

        return recur(root)



        