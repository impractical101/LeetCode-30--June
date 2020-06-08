#Submitted by thr3sh0ld
#Logic: Handling base cases first then checking the divisibility
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            if n%2 == 0:   #if perfect square will be repeatedly divisible
                n = n/2
            else:
                return False
        return True