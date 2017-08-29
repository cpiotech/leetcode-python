class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        for i in range(len(s)):
            len_1 = self.expend(s, i, i)
            len_2 = self.expend(s, i, i + 1)
            res = max(len_1, len_2)
            if res > end - start:
                start = i - (res - 1) // 2
                end = i + res // 2
        return s[start : end + 1]
        
    def expend(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1

s = Solution()
print s.longestPalindrome('babad')