#Submitted by thr3sh0ld
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        count = [0] * (amount + 1)  #initializing array with zero 
        count[0] = 1                #One's addition will always result in amount
        for i in coins:
            for j in range(i, amount + 1):
                count[j] += count[j - i]    #checking the addition in the inner loop
        return count[-1]   #returning count
        