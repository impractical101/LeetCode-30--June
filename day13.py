#Submitted by thr3sh0ld
#logic: Readable code
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        nums.sort(reverse= False)
        l = len(nums)
        count = [1 for i in range(l)]   #dp 
        prev = [-1 for i in range(l)]   #store indexing
        max_ind = 0
        for i in range(0,l):
            for j in range(i-1,-1,-1):
                if (nums[i] % nums[j] == 0):
                    if (count[i] < count[j] + 1): 
                        count[i] = count[j]+1
                        prev[i] = j 
            if (count[max_ind] < count[i]): 
                max_ind = i 
        k = max_ind 
        res = []
        while k!=-1:
            res.insert(0,nums[k])
            k=prev[k]
        return res