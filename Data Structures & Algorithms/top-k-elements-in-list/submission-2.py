class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        for _ in range (k):
            dic = {}
            for element in nums:
                if element in dic:
                    dic[element] += 1
                else:
                    dic[element] = 1
            
            maxkey = 0
            maxfreq = 0
            for key in dic:
                if dic[key] > maxfreq:
                    maxfreq = dic[key]
                    maxkey = key
            output.append(maxkey)

            nums2 = []
            for element in nums:
                if element != maxkey:
                    nums2.append(element)
            nums = nums2 
        
        return output



            
        
        


        

        


        