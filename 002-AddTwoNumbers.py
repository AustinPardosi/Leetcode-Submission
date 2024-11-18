# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Reverse int L1
        val1 = ""
        curr1 = l1
        while curr1:
            temp = val1
            val1 = str(curr1.val) + temp
            curr1 = curr1.next

        # Reverse int L2
        val2 = ""
        curr2 = l2
        while curr2:
            temp = val2
            val2 = str(curr2.val) + temp
            curr2 = curr2.next

        # jumlahkan int L1 + int L2 dan buat listNode baru
        result = str(int(val1) + int(val2))
        length = len(result)
        newList = ListNode()

        temp = newList
        while length > 0:
            temp.next = ListNode(int(result[length - 1]), None)
            temp = temp.next
            length -= 1

        return newList.next
