#Submitted by thr3s0ld
#Logic: Use counter to check the occurences.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for elements in count.elements():
            if count[elements] == 1:
                return elements