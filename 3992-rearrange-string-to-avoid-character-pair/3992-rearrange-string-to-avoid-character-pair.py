class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        a = ""
        b = ""
        c = ""
        for ch in s:
            if ch == y:
                a += ch
            elif ch == x:
                c += ch
            else:
                b += ch
        return a + b + c