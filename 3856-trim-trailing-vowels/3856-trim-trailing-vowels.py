class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        ans = s.rstrip('aeiou')
        return ans