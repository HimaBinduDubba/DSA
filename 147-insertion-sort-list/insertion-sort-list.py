# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        res=[]
        while current:
            res.append(current.val)
            current=current.next
        for i in range(1,len(res)):
            key=res[i]
            j=i-1
            while j>=0 and res[j]>key:
                res[j+1]=res[j]
                j=j-1
            res[j+1]=key
        dummy=ListNode(0)
        current1=dummy
        for i in res:
            current1.next=ListNode(i)
            current1=current1.next
        return dummy.next            


        