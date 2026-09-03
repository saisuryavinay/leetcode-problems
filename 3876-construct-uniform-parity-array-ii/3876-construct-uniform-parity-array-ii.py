class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini = min(nums1)
        if len(nums1) == 1:
            return True
        res = []
        for num in nums1:
            if mini % 2 == 1:
                if num % 2 == 1:
                    res.append(num)
                else:
                    res.append(num - mini)
            else:
                res.append(num)
        print(res)
        for ans in res:
            if ans == 0:
                return False
        for i in range(1, len(res)):
            if res[i] % 2 != res[0] % 2:
                return False
        return True