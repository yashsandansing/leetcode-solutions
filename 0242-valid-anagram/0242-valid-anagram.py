class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts = {}

        for c in s:
            counts[c] = 1 + counts.get(c, 0)

        for c in t:
            if counts.get(c) is None or counts.get(c) == 0:
                return False
            counts[c]-=1

        return True