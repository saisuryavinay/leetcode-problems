class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = 0
        cons = 0
        data = set(s)
        for val in data:
            if val in 'aeiou':
                vowel = max(vowel,s.count(val))
            else:
                cons = max(cons,s.count(val))
        return vowel+cons