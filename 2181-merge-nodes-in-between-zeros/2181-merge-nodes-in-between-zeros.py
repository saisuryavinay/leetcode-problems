class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        temp = head
        ans = 0

        while temp:
            if temp.val == 0:
                if ans != 0:
                    res.append(ans)
                    ans = 0
            else:
                ans += temp.val
            temp = temp.next

        dummy = ListNode(0)
        curr = dummy

        for x in res:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next