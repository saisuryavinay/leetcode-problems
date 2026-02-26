class Solution:
    def numSteps(self, s: str) -> int:
        ans = int(s,2)
        # print(ans)
        if ans == 1 :
            return 0
        count = 0
        while ans > 1:
            if ans % 2 == 0:
                ans = ans // 2
                count+=1
            else:
                ans = ans + 1
                count+=1
        # print(count)
        return count
