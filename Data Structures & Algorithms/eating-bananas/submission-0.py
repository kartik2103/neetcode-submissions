class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = max(piles)
        
        while l <= r:
            sum = 0
            m = (l+r)//2
            for i in range(len(piles)):
                q = (piles[i]+ m -1)//m
                sum = sum + q 
            if sum <= h:
                r = m-1
            else:
                l = m+1
        return l

        