class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        existed = [False] * 256
        max_len = 0
        i = 0
        for j in range(len(s)):
            while existed[ord(s[j])]:
                existed[ord(s[i])] = False
                i += 1
            existed[ord(s[j])] = True
            max_len = max(max_len, j - i + 1)
        return max_len

s = Solution()
print s.lengthOfLongestSubstring('abcabcbb')