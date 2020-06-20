#Submitted by thr3sh0ld
#Logic: start with (n-1)! permutations start with 1, next (n-1)! ones start with 2 and so on.
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        k -= 1
        num = [int(i) for i in range(1,n+1)]
        while n > 0:
            n -= 1
            idx, k = divmod(k, factorial(n))   # index of current digit. (return the quo and the remainder)
            ans += str(num[idx])
            #remove handled number
            num.remove(num[idx])
        return ans
