# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0(1) 1(2) 2(3) 3(None)
        # 0(None) 1(2) 2(3) 3(None)

        # 0(None) 1(0) 2(1) 3(2) [head]
        prev_node = None
        curr_node = head
        while curr_node != None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        
        return prev_node
            
            




