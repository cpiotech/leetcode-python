class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)

class Solution2(object):
    def reverseString(self, s):
        return s[::-1]

print Solution().reverseString('hello')
print Solution2().reverseString('hello')