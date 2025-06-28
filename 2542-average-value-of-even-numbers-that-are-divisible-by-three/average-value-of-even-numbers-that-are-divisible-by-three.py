class Solution:
    def averageValue(self, nums: List[int]) -> int:
        store = []
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                store.append(nums[i])
        if len(store) == 0:
            return len(store)
        return int(sum(store) / len(store))
