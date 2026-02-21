class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1
        while start <= end:
            width = end - start
            ans = min(height[end],height[start])
            area  = ans*width

            max_area = max(max_area,area)

            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        return max_area