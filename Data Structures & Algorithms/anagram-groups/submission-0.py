class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for num in strs:
            sortS = "".join(sorted(num))
            dic[sortS].append(num)
        return list(dic.values())


        

            
        
