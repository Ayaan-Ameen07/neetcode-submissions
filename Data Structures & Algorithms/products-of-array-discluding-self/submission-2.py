class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = len(nums)
        output = [1]*x

        for i in range(len(nums)):
            for j in range(len(output)):
                if i == j:
                    continue
                else:
                    output[j] *= nums[i]
        return output