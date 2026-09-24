class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        S = list(s)
        i = 0
        j = k - 1
        while i <= j:
            S[i],S[j] = S[j],S[i]
            i+=1
            j-=1
        return "".join(S)