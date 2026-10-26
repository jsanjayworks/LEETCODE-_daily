# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #print(list1,list2)
        head=None
        tail=None
        temp=list1
        k=[]
        while(temp):
            k.append(temp.val)
            temp=temp.next
        temp2=list2
        while(temp2):
            k.append(temp2.val)
            temp2=temp2.next
        k.sort()
       # print(k)
        for i in k:
            new=ListNode(i)
            if(head==None):
                head=new
                tail=new
            else:
                tail.next=new
                tail=tail.next
        return head

        