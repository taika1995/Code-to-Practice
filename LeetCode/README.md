# 单调栈
| [496.下一个更大的元素](https://leetcode-cn.com/problems/next-greater-element-i/) | [503.下一个更大的元素II](https://leetcode-cn.com/problems/next-greater-element-ii/) | [739.每日温度](https://leetcode-cn.com/problems/daily-temperatures/) | [42.接雨水](https://leetcode-cn.com/problems/trapping-rain-water/) | [84.柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) | [85.最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

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

# 堆
| [215.数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | [347.前K个高频元素素](https://leetcode-cn.com/problems/top-k-frequent-elements/) | [23.合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | [239.滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) 

## 什么时候用堆
1. 堆---处理海量数据的topK，分位数非常合适，优先队列---应用在元素优先级排序。
2. 与基于比较的排序算法 时间复杂度O(nlogn)相比，使用堆，优先队列等复杂度可以下降到O(nlogk)，在总体数据规模n较大，而维护规模k较小时，时间复杂度优化明显。

## 一些性质
1. 大顶堆，小顶堆
2. 大顶堆中每个父节点大于子节点，小顶堆每个父节点小于子节点
3. 上浮sift up: 向堆尾新加入一个元素，堆规模+1，依次向上与父节点比较，如小/大于父节点就交换。
4. 下沉sift down: 从堆顶取出一个元素（堆规模 -1，用于堆排序）或者更新堆中一个元素（本题），依次向下与子节点比较，如大于子节点就交换。

## 套路
### 上浮：
```
def sift_up(arr, child):
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val
```
### 下沉：
```
def sift_down(arr, root, k):
            val = arr[root]
            while root<<1 < k:
                child = root<<1
                if child|1 < k and arr[child|1][1] < arr[child][1]:
                    child |= 1
                if arr[child][1] < val[1]:
                    arr[root] = arr[child]
                    root = child
                else:
                    break
            arr[root] = val
```
### 库函数：
```
heapq.heappush(heap, node.val)
heapq.heappop(heap)
```
# 排序
## 归并排序
| [148.排序链表](https://leetcode-cn.com/problems/sort-list/) 
### 什么时候用？
题目要求时间空间复杂度分别为O(nlogn)和O(1)
### 套路
1. 分割cut环节
2. merge环节
#### 递归
![avatar](figures/guibing_up_to_down.png)
```
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next
```
#### 迭代
![avatar](figures/guibing_down_to_up.png)
```
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next
```

