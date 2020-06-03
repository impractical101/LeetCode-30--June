#submitted by thr3sh0ld
#Logic: Commented 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:`
        N = len(costs)//2
        if not costs:
            return
        A = [i for i,j in costs]         #sending all people to first city
        forB = [j - i for i,j in costs]  #Other half with the minimum cost to send to second city
        return sum(A) + sum(sorted(forB)[:N]) #combining the cost for bot N/2 partition
        