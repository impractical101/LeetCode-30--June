# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Submitted by thr3sh0ld
class Solution:
    def solve(self,root, curr):
        if root == None:
            return 0
        curr = curr*10 + root.val
        if not root.left and not root.right:
            return curr
        return self.solve(root.left, curr) + self.solve(root.right, curr)
        
    def sumNumbers(self,root: TreeNode) -> int:
        return self.solve(root,0)
    

        