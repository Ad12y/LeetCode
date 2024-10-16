# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recur(root, p, q):
            if not root:
                return 
            elif p.val < root.val < q.val:
                return root
            elif p.val > root.val > q.val:
                return root
            elif root.val == p.val or root.val == q.val:
                return root
            left = recur(root.left, p, q)
            right = recur(root.right, p, q)
            if left:
                return left
            else:
                return right 

        return recur(root, p, q)