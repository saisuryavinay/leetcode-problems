class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = [] * 2 * len(nums)
        for num in nums:
            res.append(num)
        for num in nums:
            ans = str(num)
            res.append(int(ans[::-1]))
        return len((list(set(res))))
