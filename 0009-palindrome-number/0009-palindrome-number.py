class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = str(x)
        for i in ans:
            if i == '-':
                return False
        i = 0
        j = len(ans) - 1
        while i < j:
            if ans[i] != ans[j]:
                return False
            i += 1
            j -= 1
        return True
            