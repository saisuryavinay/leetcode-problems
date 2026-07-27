class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, res, total = 0, 0, 0
        vowels = "aeiou"

        for i in range(len(s)):
            if s[i] in vowels:
                total += 1
            if (i - l + 1) > k:
                if s[l] in vowels:
                    total -= 1
                l += 1
            res = max(res, total)
        return res