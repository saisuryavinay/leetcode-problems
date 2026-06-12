# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        temp = head
        while temp is not None:
            res.append(temp.val)
            temp = temp.next
        print(res)

        ans = res
        res1 = ans[::-1]
        if res == res1:
            return True
        else:
            return False