# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l = {}
        next_ = head
        while next_ != None :
            if next_ in l :
                return True
            else :
                l[next_] = 0
                next_ = next_.next
        return False
        
        
