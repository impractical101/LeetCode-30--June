# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Submitted by thr3shold
#Logic: Recursively invert all leaf nodes first in left and then in right subtree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left  #invert the leaf nodes interatively
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
