class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        max_length = max(len(list1), len(list2))
        ans = []
        for i in range(max_length):
            if list1[i]:
                ans.append(list1)
            if list2[i]:
                ans.append(list2)
        return ans


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    print(s.mergeTwoLists(list1=l1, list2=l2))
