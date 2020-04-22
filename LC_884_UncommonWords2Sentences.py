class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dictionary = {}
        
        for word in A.split(" "):
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
                
        for word in B.split(" "):
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
        
        res = []
        for key, value in dictionary.items():
            if value == 1:
                res.append(key)
        return res
            
        
