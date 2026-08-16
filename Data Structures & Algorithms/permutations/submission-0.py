class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        current = []
        used_indices = set()

        def dfs(idx):
            if idx == len(nums):
                res.append(current.copy())
                return

            for i in range(len(nums)):
                if i in used_indices:
                    continue
                
                used_indices.add(i)
                current.append(nums[i])
                dfs(idx+1)
                used_indices.remove(i)
                current.pop()

        dfs(0)

        return res