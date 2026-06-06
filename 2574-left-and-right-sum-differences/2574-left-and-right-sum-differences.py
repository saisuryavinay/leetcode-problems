class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []

        for i in range(len(nums)):
            leftSum.append(sum(nums[:i]))
            rightSum.append(sum(nums[i + 1:]))

        ans = []
        for i in range(len(nums)):
            ans.append(abs(leftSum[i] - rightSum[i]))

        return ans