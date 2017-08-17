# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        sort_list = sorted(intervals, key = lambda interval : interval.start)
        res = [sort_list[0]]
        for i in range(1, len(sort_list)):
            current = sort_list[i]
            last = res[len(res) - 1]
            if current.start <= last.end:
                last.end = max(current.end, last.end)
            else:
                res.append(current)
        return res
