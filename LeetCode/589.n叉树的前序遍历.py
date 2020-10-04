#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(cur):
            if not cur:
                return           
            res.append(cur.val)
            for each in cur.children:
                dfs(each)
        
        dfs(root)
        return res
# @lc code=end

