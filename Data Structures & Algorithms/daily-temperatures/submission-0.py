class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        arr = [-1]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                arr[i] = stack[-1]
            stack.append(i)  
        result = []
        for i in range(len(temperatures)):
            result.append(max(0,arr[i]-i))
        return result
           
              
        
        