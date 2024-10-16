# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 

        res = []
        queue = [root]
        while queue:
            i = 0
            length = len(queue)
            temp = []
            while i < length:
                last = queue.pop()
                temp.append(last.val)
                if last.left:
                    queue.insert(0, last.left)
                if last.right:
                    queue.insert(0, last.right)
                i += 1
            res.append(temp)
        return res