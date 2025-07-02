import math
def signFunc(x: int) -> int:
    if x>0:
        return 1
    elif x<0:
        return -1
    return 0
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive_lst = []
        negitive_lst = []
        n = len(nums)
        for i in range(n):
            if nums[i]>0:
                positive_lst.append(nums[i])
            elif nums[i]<0 or nums[i]==0:
                negitive_lst.append(nums[i])
        #print(positive_lst)
        #print(negitive_lst)
        ans1 = math.prod(positive_lst)
        ans2 = math.prod(negitive_lst)
        new = ans1*ans2
        return(signFunc(new))