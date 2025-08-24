
#Definition of doubly linked list:
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):

        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        head.prev = dummy

        curr = head
        while curr:
            if curr.val == target:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                
                curr = curr.next
        
        return dummy.next