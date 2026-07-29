"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        curr_interval = intervals[0]
        for i in range(1,len(intervals)):
            if curr_interval.end > intervals[i].start:
                return False
            curr_interval = intervals[i]
            
            
        return True


