class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        for i in nums1:
            res.append(i)
        for j in nums2:
            res.append(j)
        res.sort()
        n = len(res)
        for i in range(n):
            if n%2==1:
                return float(res[n//2])
            else:
                m1 = res[n//2-1]
                m2 = res[n//2]
                return float(m1+m2)/2
            
            