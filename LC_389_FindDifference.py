class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        for c in t:
            if not c in map:
                return c
            else:
                map[c] -= 1
                if map[c] == 0:
                    del map[c]
        return '\0'
        
