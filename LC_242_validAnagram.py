class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        aMap = {}
        for c in s:
            if c in aMap:
                aMap[c] += 1
            else:
                aMap[c] = 1
        
        for c in t:
            if c in aMap:
                aMap[c] -= 1
                if aMap[c] == 0:
                    del aMap[c]
            else:
                return False
        return len(aMap) == 0
        
        
        
