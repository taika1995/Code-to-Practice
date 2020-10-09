#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, heap = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i+1 >= k:
                while heap and heap[0][1] < i+1-k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
# @lc code=end

