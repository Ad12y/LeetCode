# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def recur(root):
            if not root:
                return 0
            else:
                left = recur(root.left)
                right = recur(root.right)
                self.res = max(self.res, left+right)
            return max(left, right) + 1
        recur(root)
        return self.res
            
        