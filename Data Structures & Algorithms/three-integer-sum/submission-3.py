class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums) 
        res = []
        
        for i in range(len(sort)):
            if i > 0 and sort[i] == sort[i-1]:
                continue;
            
            l,r = i+1, len(sort)-1

            while l < r:
                if sort[i] + sort[l] + sort[r] > 0:
                    r -= 1
                elif  sort[i] + sort[l] + sort[r] < 0:
                    l += 1
                else:
                    res.append([sort[i], sort[l], sort[r]])
                    l += 1
                    r -= 1
                    while sort[l] == sort[l-1] and l < r:
                        l += 1
        return res



            

        