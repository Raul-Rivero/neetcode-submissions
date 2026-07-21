# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev1,cur1 = None, head

        while cur1:
            nxt = cur1.next
            cur1.next = prev1
            prev1 = cur1
            cur1 = nxt

        count = 0
        prev,cur = None, prev1

        while cur:
            count += 1
            nxt = cur.next
            if count == n:
                cur = cur.next
                continue
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
