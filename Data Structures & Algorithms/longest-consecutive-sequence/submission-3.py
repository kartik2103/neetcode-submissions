class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current = 1
        best = 1
        if not  nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
     
                current +=1
            elif nums[i]-nums[i-1]==0:

                continue
            else:
                best = max(current,best)
                current = 1
        return max(current,best)

        



        