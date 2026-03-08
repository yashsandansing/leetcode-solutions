# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        self.words = words
        
        candidates = set(words)

        while candidates:
            guess = candidates.pop()
            simil = master.guess(guess)
            if simil == 6:
                return
            candidates = {w for w in candidates if self.calculate_similarity(guess, w) == simil}
    
    
    def calculate_similarity(self, word: str, guess: str) -> int:
        sim = 0
        for w, g in zip(word, guess):
            if w == g:
                sim += 1
        
        return sim
    