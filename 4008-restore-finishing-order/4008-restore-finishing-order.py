class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for i in order:
            for j in friends:
                if i==j:
                    ans.append(j)
        return ans