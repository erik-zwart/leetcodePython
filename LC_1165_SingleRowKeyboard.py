class Solution:
    def abs(self, a: int, b: int) -> int:
        if a > b: return (a - b)
        else: return (b - a)
    
    def calculateTime(self, keyboard: str, word: str) -> int:
        dict = {}
        pos = 0
        for c in keyboard:
            dict[c] = pos
            pos += 1
        
        prevPos = 0
        ans = 0
        for c in word:
            ans += abs(dict[c] - prevPos)
            prevPos = dict[c]
        return ans
