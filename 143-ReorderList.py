# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list
        middle = slow
        second = middle.next
        middle.next = None

        # Reverse the second half
        prev, curr = None, second
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # prev is the head of second half

        # Merge the two half
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
        # Remember to not return anything -> the idea is to modify the node not to create a new one