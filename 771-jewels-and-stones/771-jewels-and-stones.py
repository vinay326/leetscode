class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list1= []
        list2= []
        list1[:0]=jewels
        list2[:0]=stones
        count = 0
        for i in list2:
            if i in list1:
                count +=1
        return count