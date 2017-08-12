# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n), n is the length of longer linked-list
# Space: O(n), n is the length of result 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = x + y + carry
            carry = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry != 0:
            p.next = ListNode(carry)
        return dummy.next
