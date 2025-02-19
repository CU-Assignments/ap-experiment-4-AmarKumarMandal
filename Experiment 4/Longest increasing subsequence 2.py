class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)
    
    def update(self, index, value):
        index += self.size  
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])
    
    def query(self, left, right):
        left += self.size
        right += self.size
        max_value = 0
        while left <= right:
            if left % 2 == 1:  
                max_value = max(max_value, self.tree[left])
                left += 1
            if right % 2 == 0: 
                max_value = max(max_value, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return max_value

class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        seg_tree = SegmentTree(max_val + 1)
        max_length = 0

        for num in nums:
            best_prev = seg_tree.query(max(1, num - k), num - 1)
            curr_length = best_prev + 1
            seg_tree.update(num, curr_length)
            max_length = max(max_length, curr_length)

        return max_length
