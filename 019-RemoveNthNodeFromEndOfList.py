# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newNode = ListNode(0, head)
        left = newNode
        right = head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return newNode.next
