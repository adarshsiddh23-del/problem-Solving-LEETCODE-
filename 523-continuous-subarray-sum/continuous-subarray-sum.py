class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict = {0: -1}
        pre_sum = 0

        for i in range(len(nums)):
            pre_sum += nums[i]
            rem = pre_sum % k

            if rem in dict:
                if i - dict[rem] >= 2:
                    return True
            else:
                dict[rem] = i

        return False 