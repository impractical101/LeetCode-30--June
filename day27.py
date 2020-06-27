#Submitted by thr3sh0ld
class Solution:
    def numSquares(self, n: int) -> int:
        arr = [0]
        if len(arr) <= n:
                Psquares = [i**2 for i in range(1, int(sqrt(n)) + 1)]
                for i in range(len(arr), n + 1):
                    arr.append(min(1 +arr[i - squares] for squares in Psquares if squares <= i))
        return arr[n]
            
            