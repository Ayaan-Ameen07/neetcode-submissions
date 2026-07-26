class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_string = "".join(filter(str.isalnum, s)).lower()
        l, r = 0, len(output_string)-1

        while l < r:
            if output_string[l] != output_string[r]:
                return False
            if output_string[l] == output_string[r]:
                l += 1
                r -= 1
        return True

                


