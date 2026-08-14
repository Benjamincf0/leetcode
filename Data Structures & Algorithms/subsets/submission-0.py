class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        def dfs(idx, current_subset):
            if idx >= len(nums): return
            subsets.append(current_subset)

            dfs(idx+1, current_subset.copy())

            current_subset.append(nums[idx])
            dfs(idx+1, current_subset.copy())

        dfs(0, [])
        
        return subsets