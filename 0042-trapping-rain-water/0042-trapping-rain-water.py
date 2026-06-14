class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        min_ans = 0
        max_ans = 0
        total = 0

        while start < end:
            min_ans = max(min_ans,height[start])
            max_ans = max(max_ans,height[end])

            if min_ans < max_ans:
                total += min_ans - height[start]
                start+=1
            else:
                total += max_ans - height[end]
                end -=1
        return total
