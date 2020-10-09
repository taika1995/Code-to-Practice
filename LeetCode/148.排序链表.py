#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# 看到复杂度带log，想到归并排序
# 递归空间复杂度高，不符合要求，需要使用迭代法替代cut
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归
        # if not head or not head.next:
        #     return head
        
        # # cut list at mid index
        # slow, fast = head, head.next
        # while fast and fast.next:
        #     fast, slow = fast.next.next, slow.next
        # mid, slow.next = slow.next, None

        # # recursive for cutting
        # left, right = self.sortList(head), self.sortList(mid)

        # # merge
        # h = res = ListNode(0)
        # while left and right:
        #     if left.val < right.val:
        #         h.next = left
        #         left = left.next
        #     else:
        #         h.next = right
        #         right = right.next
        #     h = h.next
        
        # if left:
        #     h.next = left
        # else:
        #     h.next = right
        
        # return res.next
        
        # 迭代，自底向上，不断merge，intv递增
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge in different intv
        while intv < length:
            pre, h = res, res.next
            while h:
                # get 2 merge head 'h1' 'h2'
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i-1
                if i: break # 不存在h2的头
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i-1

                c1, c2 = intv, intv-i
                # merge
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1-1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2-1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1-1, c2-1
                pre.next = h
            intv *= 2
        return res.next
                
# @lc code=end

