#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)

        for idx, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                tmp = stack.pop()
                res[tmp] = idx - tmp
            stack.append(idx)

        return res

        
# @lc code=end

