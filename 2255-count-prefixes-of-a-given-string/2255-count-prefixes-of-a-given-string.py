class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        res = []
        for i in range(1,len(s)+1):
            res.append(s[:i])
        c = 0
        for ch in words:
            if ch in res:
                c += 1
        return c