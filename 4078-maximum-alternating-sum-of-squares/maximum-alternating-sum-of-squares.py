class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted((x * x for x in nums), reverse=True)
        
        n = len(nums)
        k = (n + 1) // 2
        
        return sum(nums[:k]) - sum(nums[k:])