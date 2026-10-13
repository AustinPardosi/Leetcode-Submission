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

# Better Approach
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + carry
            carry, digit = divmod(val, 10)
            curr.next = ListNode(digit, None)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
