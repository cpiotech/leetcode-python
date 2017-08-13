# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy
        
        while current is not None and current.next is not None:
            next = current.next
            nextnext = current.next.next
            prev.next = next
            next.next = current
            current.next = nextnext
            prev = current
            current = nextnext
        
        return dummy.next
