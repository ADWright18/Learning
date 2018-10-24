# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        """
        :type node: TreeNode
        :type res: List[int]
        :rtype: void
        """
        if (node != None):
            # Append values in the following order: left, root, right
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)
