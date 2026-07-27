class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            num = str(len(s))
            res += num+"@"+s
        return res

      

    def decode(self, s: str) -> List[str]:
        
        final = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "@":
                j += 1

            length = int(s[i:j])
            final.append(s[j+1: j+1+length: 1])
            i = j +1 + length
        return final


        


       
