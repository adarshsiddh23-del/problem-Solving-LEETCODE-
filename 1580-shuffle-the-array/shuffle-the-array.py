class Solution:
    def shuffle(self, nums, n):
        return [x for pair in zip(nums[:n], nums[n:]) for x in pair]