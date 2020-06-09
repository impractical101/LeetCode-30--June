#Submitted by thr3sh0ld
#Logic: use any all to check the characters of substring in string
#Iter iterates the container once
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t) #works for any iterables, convert iterable to iterators
        return all(any(c == ch for c in it) for ch in s)
    