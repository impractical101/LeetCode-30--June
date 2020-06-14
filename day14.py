#Submitted by thr3sh0ld
#BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        cost = collections.defaultdict(list)
        minP = {src: 0}
        maxii = [src]
        for i in flights:
            cost[i[0]].append((i[1], i[2])) 
        for i in range(K+1):
            temp = set()
            copy = minP.copy()
            for j in maxii:
                for dest, amount in cost[j]:
                    if dest not in copy or copy[dest] > minP[j] + amount:
                        copy[dest] = minP[j] + amount
                        temp.add(dest)
            maxii = temp
            for c, v in copy.items():
                minP[c] = v
        return minP.get(dst, -1)
        