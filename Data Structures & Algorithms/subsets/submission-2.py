class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time O(n*2^n) ; Space O(n)
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