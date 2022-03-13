class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        j = 0
        n= len(arr)
        while j < (n-1):
            if arr[j] == 0:
                arr.insert(j+1, 0)
                arr.pop()
                j=j+2
            else:
                j=j+1
        arr = arr[:8]
                
        

                
        