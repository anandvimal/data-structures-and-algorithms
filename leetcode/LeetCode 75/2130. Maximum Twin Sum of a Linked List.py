# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = 0
        head_ptr = head
        while head_ptr:
            size += 1
            head_ptr = head_ptr.next
        print(f"size: {size}")
        half_size = size // 2
        print(f"size: {size}  and half_size: {half_size}")

        if size == 2:
            return head.val + head.next.val

        elif size >= 4:
            
            counter = 0
            head_ptr = head
            for i in range(half_size-1):
                head_ptr = head_ptr.next
                counter +=1
            print(f"counter : {counter}")

            #now head_ptr points to half
            # break halfes with none
            head2 = head_ptr.next
            head_ptr.next = None


            #here we reverse the second half of the list
            prev = None
            curr = head2
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            # prev is start of second list now
            head2 = prev

            max_sum = -1
            while head and head2:
                sum = head.val + head2.val
                max_sum = max(sum, max_sum)
                head= head.next
                head2 = head2.next
            return max_sum
        
        