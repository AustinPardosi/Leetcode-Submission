# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Cari titik tengah
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Tangkap dan pecahkan linkedlist jadi 2
        second = slow.next
        prev, slow.next = None, None

        # Reverse linkedlist second
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge Linkedlist
        list1, list2 = head, prev
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2
        return list1
