# ACCEPTED

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        res = 0
        m = len(grid)
        n  = len(grid[0])
        MOD = 10**9 + 7

        mem = {}

        def helper(r, c, curr):
            nonlocal m, n, k, MOD

            if r >= m or c >= n: return 0

            if r == m - 1 and c == n - 1:
                if curr ^ grid[r][c] == k:
                    return 1
                return 0

            if (r, c, curr) in mem:
                return mem[(r, c, curr)]

            right = helper(r, c + 1, curr ^ grid[r][c])
            down = helper(r + 1, c, curr ^ grid[r][c])

            mem[(r, c, curr)] = (right + down) % MOD
            return mem[(r, c, curr)]

        return helper(0, 0, 0)