class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        l = 0
        r = len(nums)-1
     
        while l <= r:
            if nums[l] <= nums[r]:
                mini = min(mini,nums[l])
                break
            
            m =(l+r)//2
            if nums[m] <= nums[r]:

                mini = min(mini, nums[m]) #right one is sorted
                r = m -1
            else:
                mini = min(mini,nums[r])
                l = m+1
        return mini



         


        