# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n * k * logk), Space: O(k)
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: 
            return None
        min_h = []
        for h in lists:
            if h is not None:
                heapq.heappush(min_h, (h.val, h))

        dummy = ListNode(0)
        p = dummy
        while len(min_h) != 0:
            node = heapq.heappop(min_h)[1]
            p.next = node
            p = p.next
            if node.next is not None:
                heapq.heappush(min_h, (node.next.val, node.next))

        return dummy.next
