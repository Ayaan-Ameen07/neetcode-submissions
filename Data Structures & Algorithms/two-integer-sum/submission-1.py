class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hsm = {} #key:value
       for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hsm:
            return [hsm[diff], i]
        hsm[nums[i]] = i