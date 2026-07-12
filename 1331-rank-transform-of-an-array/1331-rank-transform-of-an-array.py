class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        
        rank = {}
        for i in range(len(temp)):
            rank[temp[i]] = i + 1
        
        ans = []
        for num in arr:
            ans.append(rank[num])
        
        return ans