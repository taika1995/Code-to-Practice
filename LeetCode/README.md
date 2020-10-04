# 单调栈
| [496.下一个更大的元素](https://leetcode-cn.com/problems/next-greater-element-i/) | [503.下一个更大的元素II](https://leetcode-cn.com/problems/next-greater-element-ii/) | [739.每日温度](https://leetcode-cn.com/problems/daily-temperatures/)

## 单调栈性质
1. 单调递增栈：从 栈底 到 栈顶 递增，栈顶大
2. 单调递减栈：从 栈底 到 栈顶 递减，栈顶小

## 什么时候用单调栈
通常是一维数组，要寻找任一元素右边（左边）第一个比自己大（小）的元素，且要求 O(n) 的时间复杂度

## 套路
```
def nextGreaterElement(nums: list):
    length = len(nums)
    res, stack = [-1] * length, []

    for idx, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
        stack.append(idx)

    return res
```