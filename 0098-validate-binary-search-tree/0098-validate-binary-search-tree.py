# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lst = []
        def recur(root):
            if not root:
                return 
            recur(root.left)
            self.lst.append(root.val)
            recur(root.right)
            return 
        recur(root)
        return self.lst == sorted(self.lst) and len(self.lst) == len(set(self.lst))
        