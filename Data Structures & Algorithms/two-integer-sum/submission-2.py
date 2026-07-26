class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in bag:
                return[bag[diff], i]
            bag[n] = i
            
            

           
        
            
        


            
            

        