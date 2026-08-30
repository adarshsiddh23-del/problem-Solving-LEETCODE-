class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):

            temp = curMax

            curMax = max(nums[i],
                         curMax * nums[i],
                         curMin * nums[i])

            curMin = min(nums[i],
                         temp * nums[i],
                         curMin * nums[i])

            ans = max(ans, curMax)

        return ans