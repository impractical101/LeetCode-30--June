#Submittted by thr3sh0ld
#Logic if matched return index if note find the interval 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        for i in range(l):
            if target == nums[i]:
                return i
            if i == 0 and target < nums[i]:
                return 0
            if i != 0 and target < nums[i] and target > nums[i-1]:   #interval 
                return i
        return len(nums)