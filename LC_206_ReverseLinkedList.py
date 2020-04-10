class LinkedListIterator:
    def __init__(self, head):
        self.it_ = head
    def next(self):
        val = self.it_.val
        self.it_ = self.it_.next
        return val
    def hasNext(self):
        return self.it_ != None
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        it = LinkedListIterator(head)
        revHead = None
        while it.hasNext():
            node = ListNode(it.next())
            if revHead is None:
                revHead = node
            else:
                node.next = revHead
                revHead = node
        return revHead
