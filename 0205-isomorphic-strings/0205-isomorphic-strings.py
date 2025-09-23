class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_char = {}
        t_char = {}

        for i in range(len(s)):
            if s[i] not in s_char:
                s_char[s[i]] = i

            if t[i] not in t_char:
                t_char[t[i]] = i
            
            if s_char[s[i]] != t_char[t[i]]:
                return False

        return True