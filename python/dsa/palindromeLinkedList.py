import copy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# deque solution
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        q = deque()
        while head:
            q.append(head.val)
            head = head.next

        # if len(q) % 2 == 0:
        #     flag = 0
        # else:
        #     flag = 1

        # Tried with some cases, there no need to check for flag, we can directly check for 0 or 1
        # [1, 2, 3, 2, 1] -> [2, 3, 2] -> [3]

        while len(q) != 0:
            # print(q)
            if len(q) == 0 or len(q) == 1:
                return True

            temp = q.pop()
            temp2 = q.popleft()

            if temp != temp2:
                return False

        return True


# my own trying
class Solution:
    # node = ListNode()

    # def helper1(self, node):
    #     newL = ListNode()
    #     newL.next = node

    #     return newL

    def helper(self, dummy):
        prev = None

        while dummy:
            temp = dummy  # current equal to present node
            dummy = dummy.next
            temp.next = prev
            prev = temp

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # self.node = head
        cur = head
        prev = self.helper(head)

        # print(self.node)
        print(cur)
        print(prev)
        while cur:
            if cur == prev:
                cur = cur.next
                prev = prev.next

            else:
                return False

        return True
