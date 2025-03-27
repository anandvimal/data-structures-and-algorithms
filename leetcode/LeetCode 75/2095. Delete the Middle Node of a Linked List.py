# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        pointer = head
        while pointer != None and pointer.next !=None:
            pointer = pointer.next
            count +=1
            #print(count)
        position = count//2
        pointer = head
        
        print(f"position: {position}")
        print(f"count: {count}")
        if count == 2:
            head.next = None
            return head
        if count == 1:
            head = None
            return head
        count = 0
        while pointer != None and pointer.next !=None:
            
            if count == position -1 :
                pointer.next = (pointer.next).next
            pointer = pointer.next
            count +=1
        return head

        