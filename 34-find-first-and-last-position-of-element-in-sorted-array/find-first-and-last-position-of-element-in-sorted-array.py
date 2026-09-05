class Solution:
    def searchRange(self, nums, target):
        # First occurrence
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                if nums[mid] == target:
                    first = mid
                high = mid - 1
            else:
                low = mid + 1

        # Last occurrence
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= target:
                if nums[mid] == target:
                    last = mid
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]