# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        table = {}
        p = head
        dummy = RandomListNode(0)
        current = dummy
        while p is not None:
            current.next = RandomListNode(p.label)
            table[p] = current.next
            p = p.next
            current = current.next

        p = head
        current = dummy
        while p is not None:
            if p.random:
                current.next.random = table[p.random]
            p = p.next
            current = current.next

        return dummy.next

class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        while p is not None:
            next = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next = next
            p = next
        p = head
        while p is not None:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        p = head
        copy_head = p.next if p else None
        while p is not None:
            copy = p.next
            p.next = copy.next
            p = p.next
            copy.next = p.next if p else None
        return copy_head
