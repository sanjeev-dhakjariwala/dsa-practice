from typing import *
from ListNode import *

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList(head):
            if not head or not head.next:
                return head
            temp = reverseList(head.next)
            head.next.next = head
            head.next = None
            return temp

        fast, slow, tail = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            tail = slow
            slow = slow.next

        temp_head = slow
        tail.next = None
        temp_head = reverseList(temp_head)

        while temp_head and head:
            if temp_head.val != head.val:
                return False
            temp_head = temp_head.next
            head = head.next

        return True


head = create_linked_list_from_string("1,0,1")
sol = Solution()
print(sol.isPalindrome(head))