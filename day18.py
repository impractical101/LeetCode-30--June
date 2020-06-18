#Submitted by thr3sh0ld
#Logic:  sort desc. then set maxii value to the maximum H index while iterating.
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        maxii = 0
        for i in range(len(citations)):
            if citations[i]>maxii:
                maxii+=1
        return maxii
            
            
        