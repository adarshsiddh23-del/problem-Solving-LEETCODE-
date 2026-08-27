class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for x in nums1:
            if x in nums2:
                result.append(x)
                nums2.remove(x)

        return result
        
        