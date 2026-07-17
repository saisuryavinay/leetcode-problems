class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        o = 0
        c = 0
        res = ""
        for i in range(len(s)):
            ch = s[i]
            if ch == ')':
                o -= 1
            if o > 0:
                res += ch
            if ch == '(':
                o += 1
        return res