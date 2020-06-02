# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Submitted by thr3sh0ld
#Logic : Set the value of node to next node and mark the node poitner to next of next node

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        