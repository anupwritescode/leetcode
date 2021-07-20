# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_merged_head = ListNode(0, None)
        
        if l1 == None :
            return l2
        elif l2 == None :
            return l1
        
        if l2.val <= l1.val:
            l_merged_head = ListNode(l2.val, None)
            l2 = l2.next
        else :
            l_merged_head = ListNode(l1.val, None)
            l1 = l1.next
            
        l_merged_next = l_merged_head
        
        while l1 != None and l2 != None :
            if l2.val <= l1.val :
                l_merged_next.next = ListNode(l2.val, None)
                l2 = l2.next
            else :
                l_merged_next.next = ListNode(l1.val, None)
                l1 = l1.next
            l_merged_next = l_merged_next.next
        
        while l1 != None :
            l_merged_next.next = ListNode(l1.val, None)
            l_merged_next = l_merged_next.next
            l1 = l1.next
            
        while l2 != None :
            l_merged_next.next = ListNode(l2.val, None)
            l_merged_next = l_merged_next.next
            l2 = l2.next
            
        return l_merged_head
            
        
