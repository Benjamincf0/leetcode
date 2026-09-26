class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        l = 0
        count = 0
        for r in range(1, len(intervals)):
            if intervals[l][1] > intervals[r][0]:
                # remove whichever one ends first
                count += 1
                if intervals[l][1] < intervals[r][1]:
                    # remove right
                    pass
                else:
                    # remove left
                    l = r
            else:
                l = r
                

        return count

# (1, 3) (1, 2) (2, 3) (3, 4)
#            l  r
# count = 2