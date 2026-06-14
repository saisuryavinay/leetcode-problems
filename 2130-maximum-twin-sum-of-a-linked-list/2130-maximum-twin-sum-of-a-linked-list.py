class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next
        mid = n // 2
        temp = head
        for _ in range(mid - 1):
            temp = temp.next

        second = temp.next
        temp.next = None
        
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        ans = head
        ans1 = second
        maxi = 0

        while ans and ans1:
            maxi = max(maxi, ans.val + ans1.val)
            ans = ans.next
            ans1 = ans1.next

        return maxi