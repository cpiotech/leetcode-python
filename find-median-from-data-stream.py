'''
Before adding a new number, there are two cases: 
(small, large) == (k, k)
(small, large) == (k, k + 1)
After adding a new number : 
Add to large half (small, large) == (k, k + 1) 
Add to small half (small, large) == (k + 1, k + 1)

For first case, we can't add the new number into the large half directly. 
We should add it to small half and popup number from small half, then add it to the large half.
So we can make sure small keeps the smaller half and large keeps the larger half. 
The same as the second case, we need to add the new number into the large first and pop number, 
and add the number to small. 
'''
from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # the smaller half of the list, max-heap
        self.large = [] # the larger half of the list, min-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()