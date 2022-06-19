class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        start = 99
        end = len(wordsDict)
        min_distance = 99999
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                start = i
            elif wordsDict[i] == word2:
                end = i
        
            if start != -1 and end != -1:
                min_distance = min(min_distance, abs(start-end))
        
        return min_distance
            
        