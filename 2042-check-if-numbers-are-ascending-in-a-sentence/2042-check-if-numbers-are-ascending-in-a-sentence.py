class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = []
        for i in s.split():
            if i.isdigit():
                res.append(int(i))
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        else:
            return True