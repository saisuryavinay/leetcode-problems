class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        n = len(candies)
        max_cand = max(candies)
        for i in range(n):
            if candies[i]+extraCandies >= max_cand:
                res.append(True)
            else:
                res.append(False)
        return res