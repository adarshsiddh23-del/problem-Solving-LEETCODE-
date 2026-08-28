class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = {}
        curr = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            curr += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while freq[nums[right]] > 1:
                freq[nums[left]] -= 1
                curr -= nums[left]
                left += 1

            if right - left + 1 == k:
                ans = max(ans, curr)
                freq[nums[left]] -= 1
                curr -= nums[left]
                left += 1

        return ans