# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = []
        temp = head
        while temp:
            res.append(str(temp.val))
            temp = temp.next
        ans = "".join(res)
        return int(ans,2)