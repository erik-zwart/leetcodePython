class Stack:
    def __init__(self):
        self.list = []
    def top(self):
        return self.list[-1]
    def pop(self):
        item = self.list[-1]
        del self.list[-1]
        return item
    def push(self, item):
        self.list.append(item)
    def empty(self):
        return len(self.list) == 0
    
class Solution:        
    def removeDuplicates(self, S: str) -> str:
        stk = Stack()
        for c in S:
            if stk.empty():
                stk.push(c)
            else:
                if stk.top() == c:
                    stk.pop()
                else:
                    stk.push(c)
                    
        res = ""
        while not stk.empty():
            res = stk.pop() + res
        return res
        
        
