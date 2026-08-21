class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in nums:
            if nums in my_set:
                return True
            my_set.add(nums)
        return False


        
        