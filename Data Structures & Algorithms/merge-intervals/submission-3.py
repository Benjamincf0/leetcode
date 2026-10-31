class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if res[-1][1] < intervals[i][0]:
                # no overlap
                res.append(intervals[i])
            else:
                # yes overlap
                res[-1][1] = max(intervals[i][1], res[-1][1])

        return res

# [[1,3],[1,5],[6,7]]
#.              i
# [1,5] 