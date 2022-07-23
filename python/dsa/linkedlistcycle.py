# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash = {}
        dummy = head
        node = dummy

        while node:
            if node in hash:
                return True
            else:
                hash[node] = 1

            node = node.next

        return False
