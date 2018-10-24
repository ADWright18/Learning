# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.bfs(root, res)
        return res
        
    def bfs(self, node, res):
        """
        :type node: TreeNode
        :type res: List[int]
        :rtype: void
        """
        if (node != None):
            # Append values in the following order: left, right, root
            self.bfs(node.left, res)
            self.bfs(node.right, res)
            res.append(node.val)
