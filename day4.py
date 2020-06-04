#Submitted by thr3sh0ld
#Logic: Swap half the length of string with the other half
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]