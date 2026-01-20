class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        l = r = best = 0

        while r < len(word):
            for ind in range(r, max(r - 10, l - 1), -1):
                if word[ind: r+1] in forbidden_set:
                    l = ind + 1
                    break
            best = max(best, r - l + 1)
            r += 1
        
        return best