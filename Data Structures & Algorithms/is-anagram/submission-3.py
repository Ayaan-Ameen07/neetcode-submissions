class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = set()
        tset = set()

        for i in s:
            sset.add(i)

        for r in t:
            tset.add(r)

        if sset == tset:
            return True
        else:
            return False

            