class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c = 0
        for i in range(len(s)-1):
            if s[i] == '0' and s[i+1] == '1':
                c+=1
                # continue
            # elif s[i] == '0' and s[i+1] == '1':
            #     c+=1
        if c >= 1:
            return False
        else:
            return True