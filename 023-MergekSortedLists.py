# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Add all head into heap
        heap = []
        counter = 0
        for head in lists:
            if head:
                heapq.heappush(heap,
                    (head.val, counter, head)
                )
                counter += 1
        
        dummy = ListNode(0)
        tail = dummy
        
        # Pop from heapq the smallest value
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            # Insert the next node into the heap
            if node.next:
                heapq.heappush(heap,
                    (node.next.val, counter, node.next)
                )
                counter += 1
        return dummy.next