class Solution:
    def processStr(self, s: str, k: int) -> str:
        cnt = 0
        letter = 'abcdefghijklmnopqrstuvwxyz'
        for c in s:
            if c == '#':
                cnt *= 2
            if c == '*':
                if cnt == 0:
                    continue
                else:
                    cnt -=1
            if c in letter:
                cnt += 1
        if k >= cnt:
            return "."
        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                cnt +=1
            if s[i] == '#':
                cnt = cnt // 2
                if k >= cnt:
                    k -= cnt
            if s[i] == '%':
                k = cnt - k - 1
            if s[i] in letter:
                cnt -= 1
            if k == cnt and s[i] in letter:
                return s[i]