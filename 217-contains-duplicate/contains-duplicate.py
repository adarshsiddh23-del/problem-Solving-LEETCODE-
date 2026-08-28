class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        l1=len(set(nums))
        if l!=l1:
            return True
        else:
            return False
                 
                 