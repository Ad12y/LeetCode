# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def recur(root, max_val):
            if not root:
                return 
            if root.val >= max_val:
                print("adad")
                max_val = root.val
                self.count += 1
            recur(root.left, max_val)
            recur(root.right, max_val)
            return 
        recur(root, root.val)
        return self.count

        