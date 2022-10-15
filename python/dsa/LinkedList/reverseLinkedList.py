# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # easy solution

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        # cur = 1, 2, 3, None
        while cur:
            temp = cur.next  # temprorarily store the next values in current linkedlist | temp = 2, 3, None | temp = 3, None | temp = None
            # assign cuurent next to previous | cur.next = None | cur.next = 1 | cur.next = 2
            cur.next = prev
            prev = cur  # assign previous to current | prev = 1 | prev = 2 | prev = 3
            cur = temp  # move current to next pointer | cur = 2 | cur = 3 | cur = None
        return prev

    # tough solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
