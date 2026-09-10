class Solution:
    def subarraySum(self, nums, k):
        mp = {0: 1}
        s = ans = 0

        for x in nums:
            s += x
            ans += mp.get(s - k, 0)
            mp[s] = mp.get(s, 0) + 1

        return ans