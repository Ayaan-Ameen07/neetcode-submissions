class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
        return res == res[::-1]        
        
        
        '''
        i = 0
        j = len(s)-1
        while i < j:
            if not (s[i].isalnum() or s[j].isalnum()):
                continue;

            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
             
        return True
        
            '''

    

        