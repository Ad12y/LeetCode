# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def recur_height(root):
            if not root:
                return 0
            l = recur_height(root.left)
            r = recur_height(root.right)
            return max(l,r) + 1

        sub_h = recur_height(subRoot)

        self.lst = []

        def recur(root):
            if not root:
                return 0
            l = recur(root.left)
            r = recur(root.right)
            if max(r,l) + 1 == sub_h:
                self.lst.append(root)
            return max(r,l) + 1
        recur(root)
        
        def same_tree(p, q):
            if not p and not q:
                return True 
            elif not p:
                return False
            elif not q:
                return False
            elif p.val != q.val:
                return False
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)

        for i in self.lst:
            if same_tree(i, subRoot):
                return True
        
        return False
            
            


        