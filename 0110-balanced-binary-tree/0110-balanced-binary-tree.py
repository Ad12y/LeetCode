# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(root, res):
            if not root:
                return [True ,0]
            left = recur(root.left, res)
            right = recur(root.right, res) 
            res = abs(left[1] - right[1]) <= 1 and left[0] and right[0]
            return [res, max(left[1], right[1]) + 1]

        return recur(root, [True, 0])[0]
        