# Brute Force: Store nodes in a list
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or k == 1:
            return head

        # Store references to all nodes in an array
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        # Reverse the links of each complete group
        dummy = ListNode(0, head)
        prev_group_tail = dummy

        for start in range(0, len(nodes) - k + 1, k):
            group = nodes[start:start + k]

            # Connect the previous group to this group's new head
            prev_group_tail.next = group[-1]

            # Reverse the pointers within this group
            for i in range(k - 1, 0, -1):
                group[i].next = group[i - 1]

            # The old first node becomes the group's tail
            group[0].next = nodes[start + k] if start + k < len(nodes) else None

            prev_group_tail = group[0]

        return dummy.next