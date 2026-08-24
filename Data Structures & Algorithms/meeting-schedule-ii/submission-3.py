"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Time O(nlog(n)) ; Space O(n)
        start = sorted(map(lambda interval: interval.start, intervals))
        end = sorted(map(lambda interval: interval.end, intervals))

        i = j = 0

        max_concurrent_meetings = 0
        curr_concurrent_meetings = 0
        while i < len(intervals):
            if start[i] < end[j]:
                i+=1
                curr_concurrent_meetings += 1
            else:
                j+=1
                curr_concurrent_meetings -= 1

            max_concurrent_meetings = max(max_concurrent_meetings, curr_concurrent_meetings)

        return max_concurrent_meetings