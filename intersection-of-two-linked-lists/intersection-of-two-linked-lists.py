# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nextA = headA
        nextB = headB 
        
        l = {}
        
        while nextA != None or nextB != None :
            if nextA != None :
                if nextA in l :
                    return nextA
                l[nextA] = 0
                nextA = nextA.next
            if nextB != None :
                if nextB in l:
                    return nextB
                l[nextB] = 0
                nextB = nextB.next
        return None
