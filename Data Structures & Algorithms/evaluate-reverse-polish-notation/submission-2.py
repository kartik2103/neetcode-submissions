class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  
        for num in tokens:
            if num not in ("+","*","-","/"):
                stack.append(int(num))
            else:
                top2 = stack.pop()
                top1 = stack.pop()
                
                if num == '+':
                    stack.append(top1+top2)
                elif num == '-':
                    stack.append(top1-top2)
                elif num == '*': 
                     stack.append(top1*top2)
                elif num == '/' and top2 != 0:
                    stack.append(int(top1/top2))
        return stack[0]

            
                    
                
                        
        
        