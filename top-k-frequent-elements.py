import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table = {}
        min_heap = []
        result = []

        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
        # O(nlogk)
        for key in table:
            if len(min_heap) >= k:
                if min_heap[0][0] < table[key]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (table[key], key))
            else:
                heapq.heappush(min_heap, (table[key], key))
        for n in reversed(min_heap):
            result.append(n[1])

        return result

s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))