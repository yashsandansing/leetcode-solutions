class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        l = 0
        best = 0
        for r in range(len(s)):
            char = s[r]
            while char in characters:
                lchar = s[l]
                characters.remove(lchar)
                l += 1
            characters.add(char)
            best = max(best, r - l + 1)

        return best