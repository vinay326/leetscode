class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
              window_start, matched = 0, 0
              char_frequency = {}

              for chr in s1:
                if chr not in char_frequency:
                  char_frequency[chr] = 0
                char_frequency[chr] += 1


              for window_end in range(len(s2)):
                right_char = s2[window_end]
                if right_char in char_frequency:
                  # decrement the frequency of matched character
                  char_frequency[right_char] -= 1
                  if char_frequency[right_char] == 0:
                    matched += 1

                if matched == len(char_frequency):
                  return True

                # shrink the window by one character
                if window_end >= len(s1) - 1:
                  left_char = s2[window_start]
                  window_start += 1
                  if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                      matched -= 1
                    char_frequency[left_char] += 1

              return False



                
                
                