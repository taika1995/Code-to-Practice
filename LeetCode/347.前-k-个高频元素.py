#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 最小堆
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
        
        def sift_up(arr, child):
            val = arr[child]
            while child>>1 > 0 and val[1] < arr[child>>1][1]:
                arr[child] = arr[child>>1]
                child >>= 1
            arr[child] = val
        
        stat = collections.Counter(nums)
        stat = list(stat.items())
        heap = [(0, 0)]

        for i in range(k):
            heap.append(stat[i])
            sift_up(heap, len(heap) - 1)
        
        for i in range(k, len(stat)):
            if stat[i][1] > heap[1][1]:
                heap[1] = stat[i]
                sift_down(heap, 1, k+1)
        return [item[0] for item in heap[1:]]

# @lc code=end

