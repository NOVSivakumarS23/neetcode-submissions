"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def helper(pair):
            return pair.start
        intervals.sort(key=helper)
        prevTime = -1
        for interval in intervals:
            if interval.start<prevTime:
                return False
            prevTime = interval.end
        return True
