"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s, e = 0, 0

        res = 0 # return value
        cur = 0 # tmp value

        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                cur += 1
                res = max(res, cur)
            else:
                e += 1
                cur -= 1
            
        return res