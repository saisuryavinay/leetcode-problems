class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        maxii = 0
        for start, end in intervals:
            if end > maxii:
                count += 1
                maxii = end
        return count