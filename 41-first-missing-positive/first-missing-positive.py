class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums=set(nums)
        while ans in nums:
            ans += 1
        return ans