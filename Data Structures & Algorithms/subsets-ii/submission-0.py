class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        cur = []
        def dfs(i):
            if i == len(nums):
                res.add(tuple(sorted(cur)))
                return

            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)

        dfs(0)

        return list(res)