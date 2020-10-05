#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 2)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col + 2):
                if 1 <= j <= col:
                    if matrix[i][j-1] == '1':
                        height[j] += 1
                    else:
                        height[j] = 0
                
                while stack and height[stack[-1]] > height[j]:
                    tmp = stack.pop()
                    res = max(res, (j - stack[-1] - 1) * height[tmp])
                stack.append(j)
        return res
# @lc code=end

