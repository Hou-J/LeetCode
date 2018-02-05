# https://leetcode.com/problems/add-two-numbers/description/
#
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
#     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#     Output: 7 -> 0 -> 8
#     Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        carryOn = (l1.val + l2.val) // 10
        l1.val = (l1.val + l2.val) % 10
        while l1.next is not None and l2.next is not None:
            carryOn += l1.next.val + l2.next.val
            l1.next.val = carryOn % 10
            carryOn = carryOn // 10
            l1, l2 = l1.next, l2.next
        if l1.next is None:
            l1.next = l2.next
        while l1.next != None:
            carryOn += l1.next.val
            l1.next.val = carryOn % 10
            carryOn = carryOn // 10;
            l1 = l1.next;
        if carryOn > 0:
            l1.next = ListNode(carryOn)
        return head
