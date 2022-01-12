class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
      count = 0
      it = ['type', 'color', 'name']
      rulekey_index = it.index(ruleKey)
      for i in items:
        if i[rulekey_index] == ruleValue:
           count+=1
      return count