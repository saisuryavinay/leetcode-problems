import math
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        maxLen = 0
        for i in range(n):
            hash_set = [0] * 256
            
            for j in range(i, n):
                if hash_set[ord(s[j])] == 1:
                    break
                
                hash_set[ord(s[j])] = 1
            
                current_len = j - i + 1
                maxLen = max(maxLen, current_len)
    
        return maxLen