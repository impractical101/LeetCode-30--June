#Submitted by thr3sh0ld
#Logic: Use Counter as its mentioned there is only one duplicate number. xD
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key in count.elements():
            if count[key] >= 2:
                return key