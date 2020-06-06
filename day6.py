#Submitted by thr3sh0ld
#logic: sorting both the indexes and inserting based on the no of people before. Using insert as it is faster.
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
