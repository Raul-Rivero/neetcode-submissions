# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = {}

        cur = head

        while cur is not None:
            if seen.get(cur.val, None) == cur:
                return True
            seen[cur.val] = cur
            cur = cur.next
        
        return False
            