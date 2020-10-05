#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调栈
        # stack = []
        # res = 0

        # for idx, heigh in enumerate(height):
        #     while stack and  height[stack[-1]] < heigh:
        #         tmp = stack.pop()
        #         if len(stack) == 0:
        #             break
        #         h = min(height[stack[-1]], heigh) - height[tmp]
        #         dist = idx - stack[-1] -1
        #         res += (dist * h)
        #     stack.append(idx)
        # return res

        # 双指针
        if not height:
            return 0
        n = len(height)

        left, right = 0, n-1

        maxleft, maxright = height[0], height[n-1]

        ans = 0

        while left <= right:
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            if maxleft < maxright:
                ans += maxleft - height[left]
                left += 1
            else:
                ans += maxright - height[right]
                right -= 1
        return ans

# @lc code=end

