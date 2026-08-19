class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        right = 0
        freq = {}
       
        max_freq = 0
        for right in range(len(s)):
            if s[right] in freq:
               freq[s[right]] += 1
            else: freq[s[right]] = 1 
    
            while (right-left+1) -max(freq.values()) > k:

                freq[s[left]] -=1
                left +=1 
            ans  = max(ans, right-left+1)
        return ans



        