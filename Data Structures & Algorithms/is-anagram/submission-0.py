class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        for i in range(len(s)):
            arr.append(s[i])
        for j in range(len(t)):
            if t[j] in arr:
                return True
        return False

        