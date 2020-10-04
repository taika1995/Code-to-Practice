#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict = {}

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dict[stack.pop()] = nums2[i]
            
            stack.append(nums2[i])

        return [dict.get(x, -1) for x in nums1]
        
# @lc code=end

