class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        new = []
        for row in accounts:
            total = sum(row)
            new.append(total)
        print(total)
        return max(new)