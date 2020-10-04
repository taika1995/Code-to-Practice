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

# 二/N叉树的遍历（前，中，后，层序）
| [144.二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/) | [94.二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/) | [145.二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/) | [102.二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/) | [589.N叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/)

## 两种常规思路
1. 递归（一般在弹出操作处加其他处理）
2. 辅助栈

## 套路
### 二叉树前，中，后序遍历的递归写法
```
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return      
            # 前序递归
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right) 
            # # 中序递归
            # dfs(cur.left)
            # res.append(cur.val)
            # dfs(cur.right)
            # # 后序递归
            # dfs(cur.left)
            # dfs(cur.right)
            # res.append(cur.val)      
        res = []
        dfs(root)
        return res
```
### 二叉树前，中，后序遍历的迭代写法（辅助栈）
```
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        res = []
        stack = []
        cur = root
        # # 前序，相同模板
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        # return res

        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

        # # 后序，相同模板（一般由前序得来）
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     cur = stack.pop()
        #     cur = cur.left
        # return res[::-1]
```
### N叉树递归遍历
```
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(cur):
            if not cur:
                return           
            res.append(cur.val)
            # 逐个递归子节点
            for each in cur.children:
                dfs(each)
        
        dfs(root)
        return res
```
### 层序遍历
```
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, stack = [], collections.deque()
        stack.append(root)
        while stack:
            n = len(stack)
            res = []
            for i in range(n):
                tmp = stack.popleft()
                res.append(tmp.val)
                if tmp.left:
                    stack.append(tmp.left)
                if tmp.right:
                    stack.append(tmp.right)
            ans.append(res)
        return ans
```
