class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = bin(a)[2:]
        s2 = bin(b)[2:]
        cnt1 = 0
        cnt2 = 0
        
        for ch in s1:
            if ch == '1':
                cnt1 += 1
        for ch in s2:
            if ch == '1':
                cnt2 +=1
        if cnt1 >= cnt2:
            return cnt1 * cnt2
        else:
            return int(cnt2/cnt1)