# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # add dummy 0 so that removing an element can be easy
        dummy = ListNode(0, head)
        left = dummy

        right = head

        while right and n > 0:
            n -= 1
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


# Not correct answer but my own attempt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        pointer = p
        index, index1 = 0, 0

        while pointer:
            index1 += 1
            pointer = pointer.next

        target = index1 - n + 1
        print(index1, target)

        while pointer:
            index += 1
            if index == target:
                prev.next = pointer.next
                prev = pointer.next
                pointer = pointer.next.next

            else:
                prev = pointer
                pointer = pointer.next

        return p


# delete n th node, my own program!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        pointer = p
        index = 0
        while pointer:
            index += 1
            if index == n:
                prev.next = pointer.next
                print("#", prev.val, pointer.val)
            else:
                prev = pointer
                pointer = pointer.next
                print("^", prev.val, pointer.val)

        return p
