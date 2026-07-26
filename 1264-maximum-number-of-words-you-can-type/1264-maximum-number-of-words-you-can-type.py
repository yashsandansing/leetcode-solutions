class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # brute force method:
        # 1. store everything from brokenLetters in a set
        # 2. separate text from string to list
        # 3. for every letter in word: words, if letter in set, add +1 to count and continue to next
        words = text.split(" ")
        letters = set(brokenLetters)
        count_ = len(words)
        for word in words:
            for letter in word:
                if letter in letters:
                    count_-= 1
                    break
        
        return count_
    