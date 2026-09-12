# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We can use slow and fast
        # Utilize dummy to support remove 1st element
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        # Move the fast n+1 times
        for _ in range(n+1):
            fast = fast.next
        
        # Move it forward until fast is None
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Target remove should be on the slow.next
        slow.next = slow.next.next

        return dummy.next

# Not so optimal approach
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length of the linkedList
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        # Iterate and skip for the index of that value
        indexTarget = length - n
        i = 0

        # Use dummy approach to handle removethe first node from list
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = dummy.next
        while curr:
            nextNode = curr.next
            if i == indexTarget:
                prev.next = nextNode
            prev = curr
            curr = nextNode
            i += 1
        return dummy.next