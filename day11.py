#Submitted by thr3sh0ld
#Logic: Just a normal bubble sort or for fun or if you lazy just usr "sort()"
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums) 
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j+1]< nums[j]:
                    temp=nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
    