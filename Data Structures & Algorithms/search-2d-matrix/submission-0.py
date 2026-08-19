class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in matrix:
            for j in i:
                arr.append(j)
        
        l = 0
        r = len(arr)-1
        while l <= r:
            m = (l+r)//2
            if arr[m] == target:
                return True
            elif arr[m]<target:
               l =  m+1
            else:
                r = m-1
        return False


