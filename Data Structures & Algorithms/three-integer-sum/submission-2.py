class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums) 
        j = 1
        k = len(sort)-1
        res = []

        for i in sort:
            while i < k:
                if sort[i]+sort[k] == -(sort[i]):
                    res.append([sort[i], sort(j), sort(k)])
                elif sort[i]+sort[k] > -(sort[i]):
                    k -= 1
                elif sort[i]+sort[k] < -(sort[i]):
                    j += 1
        return []

            

        