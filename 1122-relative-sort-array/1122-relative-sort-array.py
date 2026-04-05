class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    new.append(arr1[j])
        remaining = []
        for j in range(len(arr1)):
            if arr1[j] not in arr2:
                remaining.append(arr1[j])
        remaining.sort()
        new.extend(remaining)
        return new