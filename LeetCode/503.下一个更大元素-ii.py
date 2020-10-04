#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums * 2
        stack = []
        res = [-1] * len(nums)

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(idx)

        return res[:len(nums)//2]
        
# @lc code=end

