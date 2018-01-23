# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        i = head
        while i.next:
            if i.val == i.next.val:
                i.next = i.next.next
            else:
                i = i.next
        return head