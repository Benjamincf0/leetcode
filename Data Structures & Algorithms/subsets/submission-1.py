class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        subset = []

        def dfs(idx):
            if idx >= len(nums):
                subsets.append(subset.copy())
                return

            dfs(idx+1)

            subset.append(nums[idx])
            dfs(idx+1)

            subset.pop()

        dfs(0)
        
        return subsets