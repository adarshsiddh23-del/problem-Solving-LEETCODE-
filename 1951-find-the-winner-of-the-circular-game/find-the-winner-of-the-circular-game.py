class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        j=0
        for i in range(1,n+1):
            j=(j+k)%i
        return j+1

       

             

        
        