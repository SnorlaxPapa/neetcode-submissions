"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        intuitive: sort in nlogn, then check for non overlappig
        """
        if not intervals: return True

        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < prev:
                return False
            prev = intervals[i].end

        return True