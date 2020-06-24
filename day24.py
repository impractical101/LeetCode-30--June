#Submitted by thr3sh0ld
#Logic: Felt lazy, hence used the formula to calculate. xD
class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2*n) // (factorial(n+1)*factorial(n))
        