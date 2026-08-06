# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memory=set()
        while head!=None:
            v= head
            if v in memory:
                return True
            else:
                memory.add(v)
            head=head.next
        return False
            