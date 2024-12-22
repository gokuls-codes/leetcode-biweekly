# BRUTE FORCE
# TLE, 750/947 test cases passed

class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:

        n = len(nums)
        res = 0

        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c + 1, n):
                        for e in range(d + 1, n):
                            mem = Counter([nums[a], nums[b], nums[c], nums[d], nums[e]])
                            maxOcc = max(mem.values())
                            numModes = 0
                            mode = 0
                            for key in mem:
                                if mem[key] == maxOcc: 
                                    numModes += 1
                                    mode = key
                            if numModes > 1: continue
                            if mode != nums[c]: continue
                            res += 1

        return res
                            