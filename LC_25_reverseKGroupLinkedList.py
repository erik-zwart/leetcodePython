class Stack:
    def __init__(self):
        self.list, self.size = [], 0
    def top(self):
        assert len(self.list) > 0
        return self.list[-1];
    def pop(self):
        assert len(self.list) > 0
        del self.list[-1]
        self.size -= 1
    def push(self, val):
        self.list.append(val)
        self.size += 1
    def empty(self):
        return len(self.list) <= 0
    def size(self):
        return self.size

def getReverseList(stk):
    head, tail = None, None
    while not stk.empty():
        node = stk.top()
        stk.pop()
        if head is None:
            head, tail = node, node
        else:
            tail.next = node
            tail = node
        tail.next = None
    return head, tail
def getForwardList(stk):
    head, tail = None, None
    while not stk.empty():
        node = stk.top()
        stk.pop()
        if head is None:
            head, tail = node, node
            head.next = None
        else:
            node.next = head
            head = node
    return head, tail

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stk = Stack()
        curr = head
        nh, nt = None, None
        
        while curr is not None:
            remaining = k
            while remaining > 0 and curr is not None:
                stk.push(curr)
                curr = curr.next
                remaining -= 1
            h, t = None, None
            if stk.size == k:
                h, t = getReverseList(stk)
            else:
                h, t = getForwardList(stk)
            if nh is None:
                nh, nt = h, t
            else:
                nt.next, nt = h, t
        return nh
