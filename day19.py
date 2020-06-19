#Submitted by thr3s0ld
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def check(mid, roll):
            a = 0
            for i in range(mid):
                a = (a * 26 + ans[i]) % roll
            dic = {a}
            aL = pow(26, mid, roll)
            for pos in range(1, n - mid + 1):
                a = (a * 26 - ans[pos - 1] * aL + ans[pos + mid - 1]) % roll
                if a in dic:
                    return pos
                dic.add(a)
            return -1
        n = len(S)
        ans = [ord(i) - ord('a') for i in S]
        lo, hi = 1, n
        pos = -1
        roll = 2**63 - 1
        #binary
        while lo <= hi:
            mid = (lo + hi) // 2
            cur = check(mid, roll)
            if cur != -1:
                lo = mid + 1
                pos = cur
            else:
                hi = mid - 1
        return S[pos: pos + lo - 1]
        
        