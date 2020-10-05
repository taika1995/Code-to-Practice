#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0

        for idx, heigh in enumerate(heights):
            while stack and heights[stack[-1]] > heigh:
                tmp = stack.pop()
                res = max(res, (idx - stack[-1] - 1) * heights[tmp])
            stack.append(idx)
        return res
# @lc code=end

