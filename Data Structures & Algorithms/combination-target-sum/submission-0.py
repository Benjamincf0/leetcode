class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        current = []

        def dfs(idx: int, running_total: int):
            if running_total == target:
                res.append(current.copy())
                return
            elif idx >= len(nums) or running_total > target: return

            # Skip this number
            dfs(idx+1, running_total)

            # Choose this number ... and maybe we'll choose it again later.
            current.append(nums[idx])
            dfs(idx, running_total+nums[idx])

            # backtrack
            current.pop()
        
        dfs(0, 0)

        return res