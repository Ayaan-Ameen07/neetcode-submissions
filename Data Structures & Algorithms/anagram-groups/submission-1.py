class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       srt = []
       for i in strs:
        srt.append(sorted(i))
       for i in srt:
        i.join("")
        
