class Solution:
    def numOfStrings(self, pat: List[str], word: str) -> int:
        ans = word.split()
        c = 0
        for i in pat:
            if i in word:
                c += 1
        return c