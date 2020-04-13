class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rowMap = {0: "qwertyuiop",
                 1: "asdfghjkl",
                 2: "zxcvbnm"}
        ans = []
        for word in words:
            prevRow = -1
            sameRow = True
            for c in word:
                r = -1
                for i in range(0, 3):
                    if c in rowMap[i] or c in rowMap[i].upper():
                        r = i
                        break
                if prevRow == -1:
                    prevRow = r
                elif prevRow != r:
                    sameRow = False
                    break
            if sameRow:
                ans.append(word)
        
        return ans
                    
