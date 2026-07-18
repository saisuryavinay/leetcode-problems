class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list(s)
        start = 0
        end = len(ans) - 1
        vowels = "aeiouAEIOU"

        while start < end:
            if ans[start] not in vowels:
                start += 1
            elif ans[end] not in vowels:
                end -= 1
            else:
                ans[start], ans[end] = ans[end], ans[start]
                start += 1
                end -= 1
        return "".join(ans)