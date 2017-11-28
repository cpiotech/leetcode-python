'''
1. Sorted the array, then return nums[len(nums) - k]. T: O(nlogn), S: O(1) with in-place sorting
2. Use min-heap to track k element. T: O(nlogk), S: O(k)
3. Selection algorithm (based on the partition method which is used in quick sort). T: O(n), S: O(1)
'''
from heapq import *

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for n in nums:
            if len(h) < k:
                heappush(h, n)
            else:
                if n > h[0]:
                    heappop(h)
                    heappush(h, n)
        return heappop(h)

s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))