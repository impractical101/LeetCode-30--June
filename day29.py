#Submitted by thr3sh0ld 
#Logic: using dp. Ways to reach the point mat[i][j]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1
        mat = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i][j-1]+mat[i-1][j]
        return mat[-1][-1]
        