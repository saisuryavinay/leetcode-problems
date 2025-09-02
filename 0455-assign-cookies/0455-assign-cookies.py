class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0
        count = 0
        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                count += 1
                i += 1
        return count