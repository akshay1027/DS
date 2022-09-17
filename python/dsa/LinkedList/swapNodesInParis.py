class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            cur = prev.next  # 1
            adj = cur.next  # 2
            prev.next, cur.next, adj.next = adj, adj.next, cur  # 1 -> 2,
            prev = cur
        return dummy.next
