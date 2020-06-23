# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Submitted by thr3sh0ld 
#Logic:  Using recursion travel left and right, meanwhile update the value of count while traversing.
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def size(root):
            count = 1
            if root is not None:
                if root.left is not None:
                    count += size(root.left)
                if root.right is not None:
                    count += size(root.right)
            return count
        ans = size(root)
        return ans 
        