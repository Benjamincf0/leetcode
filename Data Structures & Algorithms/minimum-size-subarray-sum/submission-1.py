class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        m_len = len(nums)+1
        cur_sum = 0

        while l <= r < len(nums)+1:

            if cur_sum >= target:
                cur_sum -= nums[l]
                l += 1
                m_len = min(m_len, r-l+1)
            else:
                if r == len(nums): break
                cur_sum += nums[r]
                r += 1

        return m_len if m_len < len(nums)+1 else 0

# target = 11
# 1 2 3 4 5
#         l
#           r
# cur_sum = 1+2+3+4+5-1-2
# m_len = 6