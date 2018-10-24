# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
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
            # Add the root
            res.append(node.val)

            # Then the left side of the tree
            self.dfs(node.left, res)

            # Lastly, the right side of the tree
            self.dfs(node.right, res)
