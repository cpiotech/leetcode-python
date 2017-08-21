class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + 1
            if s <= 9:
                digits[i] = s
                return digits
            else:
                digits[i] = 0

        digits.append(0)
        digits[0] = 1

        return digits