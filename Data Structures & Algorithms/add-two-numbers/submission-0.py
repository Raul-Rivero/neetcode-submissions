# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1, list2 = [],[]

        cur = l1
        while cur:
            list1.insert(0,str(cur.val))
            cur = cur.next
        
        cur = l2
        while cur:
            list2.insert(0,str(cur.val))
            cur = cur.next

        num1 = "".join(list1)
        num1 = int(num1)

        num2 = "".join(list2)
        num2 = int(num2)

        num3 = num1 + num2
        num3 = str(num3)

        dummy = ListNode()
        node = dummy

        for i in range(len(num3) - 1, -1, -1):
            node.next = ListNode(int(num3[i]))
            node = node.next

        return dummy.next


