# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Submitted by thr3sh0ld 
#Logic:  A very clean logic in BST if val is less than root traverse left if not traverse right.
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif val < root.val:   #finding the root val
                root = root.left
            else: root = root.right
        return root
            
        