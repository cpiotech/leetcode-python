# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -sys.maxsize, sys.maxsize)

    def isValid(self, node, low, high):
        if node == None:
            return True
        return node.val > low and \
               node.val < high and \
               self.isValid(node.left, low, node.val) and \
               self.isValid(node.right, node.val, high)
    