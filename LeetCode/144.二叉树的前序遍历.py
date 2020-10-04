#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        res = []
        # 双栈迭代
        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     cur = cur.right
        
        # 递归
        def dfs(cur):
            if not cur:
                return
            res.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(root)
        return res      
      
# @lc code=end

