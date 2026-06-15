# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        c = 0
        temp = head
        while temp:
            c += 1
            temp = temp.next
        print(c)
        mid = c // 2
        temp = head
        for _ in range(mid - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head