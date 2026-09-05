class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        curr_sum = 0
        tot = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                tot += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1
        return tot