class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_repeated_count = 0, 0
        char_freq = {}
        max_length = 0
        
        
        for window_end in range(len(s)):
            char = s[window_end]
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] +=1
            max_repeated_count = max(max_repeated_count, char_freq[char])
            
            x = window_end - window_start+1 - max_repeated_count
            
            if x > k:
                left_char = s[window_start]
                char_freq[left_char] -=1
                window_start +=1
                
            max_length = max(max_length, window_end -window_start+1)
            
        return max_length
                
            
            
            