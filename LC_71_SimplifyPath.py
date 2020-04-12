class Solution:
    def simplifyPath(self, path: str) -> str:
        
        ansList = []
        for t in path.split('/'):
            if t == "":
                continue
            elif t == "..":
                if len(ansList) > 0:
                    del ansList[-1]
            elif t == ".":
                continue
            else:
                ansList.append(t)
                
        ans = "/"
        for a in ansList:
            ans += a
            ans += "/"
        if len(ans) > 1:
            ans = ans[:len(ans) - 1]
        return ans
            
        
