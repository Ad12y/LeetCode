# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(root, l):
            if not root:
                return l
            else:
                left = recur(root.left, l+1)
                right = recur(root.right, l+1)

            return max(left, right)

        return recur(root, 0)

        