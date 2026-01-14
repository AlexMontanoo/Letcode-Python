# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited={}
        currenta=headA
        currentb=headB
        while currenta:
            visited[currenta]=True
            currenta=currenta.next
        while currentb:
            if currentb in visited:
                break
            currentb=currentb.next    
        return currentb