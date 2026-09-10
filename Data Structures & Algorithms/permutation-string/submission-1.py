class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        n = len(s1)
        l = 0

        for r in range(1,len(s2)+1):
            c2 = Counter(s2[l:r])

            if c1 == c2:
                return True
            
            if (r - l + 1) > n:
                l += 1

        return False
