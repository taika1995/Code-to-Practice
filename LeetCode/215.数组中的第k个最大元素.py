#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 库函数
        # import heapq
        # heap = []
        # heapify(heap)
        # for num in nums:
        #     heappush(heap, num)
        #     if len(heap) > k:
        #         heappop(heap)
        # return heap[0]

        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right < max_len and nums[max_loc] < nums[right]:
                max_loc = right
            if max_loc != idx:
                nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
                adjust_heap(max_loc, max_len)
        
        n = len(nums)
        for i in range(n//2-1, -1, -1):
            adjust_heap(i, n)
        print(nums)
        
        res = None
        for i in range(1, k+1):
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0, n-i)
            print(nums)
        return res
# @lc code=end

