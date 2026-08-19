class Solution:
    def maxArea(self, heights: List[int]) -> int:
      #  for i in range(len(heights)):
            left = 0
            right = len(heights)-1
            area = float('-inf')
            while left<right:
                gap = min(heights[left],heights[right])
                max_area = gap*(right-left)
                if max_area > area:
                    area = max_area
                
                if heights[left]<heights[right]:
                    left+=1
                else:
                    right-=1

            return area


        