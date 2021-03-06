# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.swap(head)
        
    def swap(self,head):
        if not head or not head.next:
            return head
        temp = head.val
        head.val= head.next.val
        head.next.val= temp
        self.swap(head.next.next)
        return head
