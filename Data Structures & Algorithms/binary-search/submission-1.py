class Solution:
    def search(self, nums: List[int], target: int) -> int:
       mid = len(nums)//2
       l = 0
       r = len(nums) -1

       while l <= r:

        if nums[mid] < target:
            l = mid+1
            mid = len(nums[l::])//2

        elif nums[mid] > target:
            r = mid - 1
            mid = len(nums[:r:])//2
                
        else:
            return mid
       return -1 
    

        