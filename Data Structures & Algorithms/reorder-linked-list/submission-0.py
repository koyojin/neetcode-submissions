#0113

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes=[]
        cur=head
        while cur:
            nodes.append(cur)
            cur=cur.next
        n=len(nodes)
        for i in range(len(nodes)//2):
            nodes[i].next=nodes[n-1-i]
            nodes[n-1-i].next=nodes[i+1]
        nodes[n//2].next=None


