#Submitted by thr3sh0ld 
#Using DFS 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(list)
        for flight in tickets:
            dic[flight[0]] += flight[1],
        self.route = ["JFK"]
        def dfs(start = 'JFK'):
            dist = sorted(dic[start])
            for dst in dist:
                dic[start].remove(dst)
                self.route += dst,
                dfs(dst)
                if len(self.route) == len(tickets) + 1:
                    return self.route
                self.route.pop()
                dic[start] += dst,
        return dfs()
        