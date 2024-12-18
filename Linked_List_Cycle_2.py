#142 Linked List Cycle II
"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
Note that pos is not passed as a parameter.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head

        #Use Hare-Tortoise Algorithm
        #Use one 'slow' and one 'fast' pointer, the node where they meet is the start of the cycle
        #if fast never catches up to slow then there is no cycle
        """
        :type head: ListNode
        :rtype: ListNode
        """
