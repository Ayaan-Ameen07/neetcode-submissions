class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')':'(' , '}' : '{' , ']':'[' }

        for element in s:
            if element in pairs:
                if stack and stack[-1] == pairs[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        
        return True if not stack else False