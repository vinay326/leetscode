class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic ={}
        r=""
        for i in range(0, len(s)):
            dic[indices[i]] = s[i]
        
        for i in range(0, len(s)):
            r += dic[i]

        return r