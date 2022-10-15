# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initiase new LL
        ans = ListNode()
        # Pointer to the LL (ans)
        cur = ans

        slow, fast = head, head

        while fast and fast.next:
            cur.next = slow
            slow = slow.next
            fast = fast.next.next
            cur = cur.next

        cur.next = slow.next

        return ans.next
