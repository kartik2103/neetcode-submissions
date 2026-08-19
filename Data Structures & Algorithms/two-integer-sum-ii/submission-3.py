class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(numbers)):
            a = numbers[i]
            b = target - a
            if b in temp:
                return [temp[b] + 1,i + 1]
            
            else:
                temp[a] = i





            

        