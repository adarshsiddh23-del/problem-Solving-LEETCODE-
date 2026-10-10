class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        low, high = 0, max(diff)

        while low < high:
            mid = (low + high) // 2

            if sum(max(0, d - mid) for d in diff) <= k:
                high = mid
            else:
                low = mid + 1

        limit = low
        ans = 0
        remaining = k

        for d in diff:
            if d > limit:
                remaining -= d - limit
                ans += limit * limit
            else:
                ans += d * d

        return ans - remaining * (2 * limit - 1)