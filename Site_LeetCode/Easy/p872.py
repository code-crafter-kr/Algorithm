# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        def DFS(root):
            if not root:
                return []
            
            if not root.left and not root.right:
                return [root.val]
            
            return DFS(root.left) + DFS(root.right)

        return DFS(root1) == DFS(root2)