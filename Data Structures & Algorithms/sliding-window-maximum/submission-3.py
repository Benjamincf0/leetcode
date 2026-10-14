class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mq = deque()
        res = []

        for i in range(len(nums)):
            while mq and nums[mq[-1]] < nums[i]:
                mq.pop()

            if mq and mq[0] <= i-k:
                mq.popleft()
                
            mq.append(i)

            if i+2 > k and mq:
                res.append(nums[mq[0]])

        return res