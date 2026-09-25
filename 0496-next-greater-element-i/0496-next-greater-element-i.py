class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            val = nums2.index(num)
            greater = -1
            for i in range(val + 1, len(nums2)):
                if nums2[i] > num:
                    greater = nums2[i]
                    break
            res.append(greater)
        return res