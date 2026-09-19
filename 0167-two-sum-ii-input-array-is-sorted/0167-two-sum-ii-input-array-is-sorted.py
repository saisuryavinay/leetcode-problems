class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i <= j:
            sumi = numbers[i] + numbers[j]
            if sumi == target:
                return [i + 1,j + 1]
            elif sumi > target:
                j -= 1
            else:
                i += 1