class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0

        mp = {0: -1}

        for i in range(len(nums)):

            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in mp:
                max_len = max(max_len, i - mp[count])
            else:
                mp[count] = i

        return max_len