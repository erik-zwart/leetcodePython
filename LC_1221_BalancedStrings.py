class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCount = 0
        rCount = 0
        i = 0
        ans = 0
        
        while i < len(s):
            if s[i] == 'L': lCount += 1
            else: rCount += 1
            if lCount == rCount:
                ans += 1
                lCount = 0
                rCount = 0
            i += 1
        return ans
