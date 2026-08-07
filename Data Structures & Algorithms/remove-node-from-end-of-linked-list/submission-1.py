# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[ListNode(0)]
        cur=head
        while cur:
            nodes.append(cur)
            cur = cur.next
        nodes[0].next=nodes[1]
        nodes.append(ListNode(0))
        nodes[-2].next=nodes[-1]
        
        for i in range(1,len(nodes)-1):
            if i == len(nodes)-n-1:
                nodes[i-1].next=nodes[i+1]
                nodes[i].next=None

                last = nodes[-3] if i == len(nodes) - 2 else nodes[-2]
                last.next = None

        return nodes[0].next