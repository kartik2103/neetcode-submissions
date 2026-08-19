class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        for i in range(len(nums)):
            if nums[i]  in bucket:
                bucket[nums[i]] += 1
            else :
                 bucket[nums[i]] = 1
        ans = []
        for _ in range(k):          
            max_key = max(bucket, key= bucket.get)

            ans.append(max_key)
            del bucket[max_key]
        return ans

