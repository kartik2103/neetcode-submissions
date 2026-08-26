class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_var = -1
        left_side_max = [0] * n
        right_side_max = [0] * n
        ans = 0
        # final = [0] * n
        for i in range(n):
            max_var = max(max_var,height[i])
            left_side_max[i] = max(height[i],max_var)
        
        max_var = -1
        for j in range(n-1,-1,-1):
            max_var = max(max_var, height[j])
            right_side_max[j] = max(height[j],max_var)
        
        for i in range(n):
            val = min(left_side_max[i],right_side_max[i]) - height[i]
            ans = ans + val
        
        return ans


        
        
               
        