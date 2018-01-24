# https://leetcode.com/problems/reverse-linked-list/description/
#
# Reverse a singly linked list.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        r = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return r