class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x = 0
        for i in sentences:
            y = len(i.split())
            if y>x:
                x=y
        return x
        