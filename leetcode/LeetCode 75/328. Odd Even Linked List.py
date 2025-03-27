# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        odd_pointer = odd
        even_pointer = even

        index =1

        while head != None:
            if index %2 == 1:
                odd_pointer.next = head
                odd_pointer = odd_pointer.next
            elif index % 2 ==0:
                even_pointer.next = head
                even_pointer = even_pointer.next
            print(head.val)
            head = head.next
            index +=1
        even_pointer.next = None
        odd = odd.next
        even= even.next
        odd_pointer.next = even
        return odd
        