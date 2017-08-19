class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [False] * (len(nums) + 1)
        for n in nums:
            l[n] = True
        for i in range(len(l)):
            if not l[i]:
                return i
        return -1

class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = ( n * ( n + 1 ) ) // 2
        r = sum(nums)
        return s - r