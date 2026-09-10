class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict = {0:1}
        pre_sum = 0
        count = 0

        for x in nums:
            pre_sum += x
            rem = pre_sum % k

            if rem in dict:
                count += dict[rem]
                dict[rem] += 1
            else:
                dict[rem] = 1

        return count