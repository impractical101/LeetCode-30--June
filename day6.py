#Submitted by thr3sh0ld
#Logic: Just understand the concept of randomly pick the index in proportion to the weight
#Calculate the proprtion by calculating the probab of each occurence and distribute it in /
#the intervals of the proportion
class Solution:
    def __init__(self, w: List[int]):
        self.arr = [] 
        sum = 0 
        for i in w:
            sum+=i
            self.arr.append(sum)  #regions
        self.final = sum
    
    def pickIndex(self) -> int:
        rand = self.final * random.random()
        low, high = 0, len(self.arr)
        while low < high:           # Binary search: can use jump search with binary
            mid = low + (high - low) // 2
            if rand > self.arr[mid]:
                low = mid+1
            else: high = mid
        return low
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()