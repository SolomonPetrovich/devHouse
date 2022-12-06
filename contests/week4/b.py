# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        cur = head
        while True:
            cur = cur.next
            size += 1
            if not cur:
                break
    
        new = temp = head
        count = 1
        while True:
            if count == size - n + 1:
                temp = temp.next.next
            if temp:
                temp = temp.next
            count += 1

        return new.next

l1, l2, l3, l4, l5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
l1.next, l2.next, l3.next, l4.next = l2, l3, l4, l5

print(Solution().removeNthFromEnd(l1, 2))
