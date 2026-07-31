class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums)+1)]
        res = []

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        for z,v in freq.items():
            bucket[v].append(z)
        
        for n in range(len(bucket) -1, -1, -1):
            for s in bucket[n]:
                res.append(s)
                if len(res) == k:
                    return res
                
        

        




        