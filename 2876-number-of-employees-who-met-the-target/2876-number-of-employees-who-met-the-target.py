class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = 0
        n = len(hours)
        for i in range(n):
            if hours[i] >= target:
                c+=1
        return c
      