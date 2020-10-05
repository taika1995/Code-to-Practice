#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == "[":
                stack.append([multi, res])
                multi = 0
                res = ""
            elif c == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif c >= "0" and c <= "9":
                multi = multi * 10 + int(c)
            else:
                res += c
        return res
# @lc code=end

