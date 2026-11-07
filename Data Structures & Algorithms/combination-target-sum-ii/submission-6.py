class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        l = []
        res = []

        def backtrack(i, s):
            if s == target:
                res.append(l.copy())
                return
            if i == len(candidates) or s>target:
                return

            l.append(candidates[i])
            backtrack(i+1, s+candidates[i])
            l.pop()
            j = 0
            while i+j<len(candidates) and candidates[i+j] == candidates[i]:
                if s + candidates[i+j] > target:
                    return
                j += 1

            if i+j<len(candidates):
                backtrack(i+j, s)

        backtrack(0, 0)

        return res