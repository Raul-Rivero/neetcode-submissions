# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        cur = prev
        prev = None
        count = 0

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