class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in check_dict:
                if stack and stack[-1] == check_dict[c]:
                   stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

            
