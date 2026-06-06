class Solution:
    def merge(self,arr,low,mid,high):

        left = low
        right = mid + 1
        res = []
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                res.append(arr[left])
                left+=1
            else:
                res.append(arr[right])
                right+=1
        while left <= mid:
            res.append(arr[left])
            left+=1
        while right <= high:
            res.append(arr[right])
            right+=1

        for i in range(low, high + 1):
            arr[i] = res[i - low]
    
    def count_p(self, nums, low, mid, high):
        right = mid + 1
        cnt = 0

        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            cnt += right - (mid + 1)

        return cnt

    def ms(self,arr,low,high):

        if low >= high:
            return 0
        
        mid = (low + high)//2
        c = 0
        c += self.ms(arr,low,mid)
        c += self.ms(arr,mid+1,high)
        c += self.count_p(arr,low,mid,high)
        self.merge(arr,low,mid,high)

        return c

    def reversePairs(self, nums):
        n = len(nums)
        return self.ms(nums,0,n-1)
