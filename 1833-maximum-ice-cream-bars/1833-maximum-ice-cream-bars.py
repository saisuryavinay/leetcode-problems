class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        c = 0
        for cost in costs:
            total += cost
            if total <= coins:
                c += 1
        return c