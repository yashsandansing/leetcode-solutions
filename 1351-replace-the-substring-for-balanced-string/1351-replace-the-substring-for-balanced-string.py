class Solution:
    def balancedString(self, s: str) -> int:
        counts = Counter(s)
        n = len(s) // 4
        extras = dict()

        for k, v in counts.items():
            while v > n:
                extras[k] = extras.get(k, 0) + 1
                v -= 1
        
        i = 0
        best = len(s)
        if not extras:
            return 0
        for j in range(len(s)):
            if s[j] in extras:
                extras[s[j]] -= 1
            
            while max(extras.values()) <= 0:
                best = min(best, j - i + 1)
                if s[i] in extras:
                    extras[s[i]] += 1
                i += 1
        
        return best