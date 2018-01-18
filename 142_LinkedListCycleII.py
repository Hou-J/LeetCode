# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Note: Do not modify the linked list.
#
# Follow up:
# Can you solve it without using extra space?

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        result = None
        while slow is not None and fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                result = fast
                break
        while result is not None:
            if result == head:
                return result
            result = result.next
            head = head.next
        return None