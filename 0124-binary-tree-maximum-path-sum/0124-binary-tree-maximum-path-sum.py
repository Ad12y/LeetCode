# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val = float('-inf')
        def recur(root):
            if not root:
                return 0
            l = recur(root.left)
            r = recur(root.right)
            val = root.val
            if val + l > val:
                val += l
            if val + r > val:
                val += r
            print(val)
            self.max_val = max(val, self.max_val)
            return max(0, max(l, r) + root.val)
        recur(root)
        return self.max_val


        