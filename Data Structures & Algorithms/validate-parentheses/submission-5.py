class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)    
            else:
                if not stack:
                    return False 
                    
                top = stack.pop();
                if (i == '}' and top == '{'):
                    continue 
                elif (i==')' and top == '('): 
                    continue 
                elif (i==']' and top == '['):
                    continue 
                else:
                    return  False 
        if not stack:
            return True  
        else:
            return False        
            
            
                
        