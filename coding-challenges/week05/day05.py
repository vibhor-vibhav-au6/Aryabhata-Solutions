class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d ={}
        s2 = ''
        for i in range(len(indices)):
            d[indices[i]] = s[i]
            
        for i in range(len(indices)):
            s2 = s2+ d[i]
            
        return s2
            