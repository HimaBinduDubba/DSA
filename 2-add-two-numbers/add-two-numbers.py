# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1=l1
        current2=l2
        s1=""
        s2=""
        res=0
        while current1:
            s1=s1+str(current1.val)
            current1=current1.next
        while current2:
            s2=s2+str(current2.val)
            current2=current2.next 
        s1_int=int(s1[::-1])
        s2_int=int(s2[::-1])
        res=s1_int+s2_int
        res_str=str(res)
        res_str=res_str[::-1]
        dummy=ListNode(0)
        current=dummy
        for i in res_str:
            current.next=ListNode(int(i))
            current=current.next
        return dummy.next  

        
        