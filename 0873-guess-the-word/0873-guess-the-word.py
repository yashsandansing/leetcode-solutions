# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        while words:
            best = self.bestGuess(words)
            score = master.guess(best)
            if score == 6:
                return
            words = [w for w in words if self.getSimilarity(best, w) == score]
    
    def getSimilarity(self, word1: str, word2: str) -> int:
        sim = 0
        for i, j in zip(word1, word2):
            if i == j:
                sim += 1
        return sim
    
    def bestGuess(self, candidates: List[str]) -> str:
        best = candidates[0]
        min_worst = float('inf')
        for guess in candidates:
            scoreBuckets = defaultdict(int)

            for word in candidates:
                similarity = self.getSimilarity(guess, word)
                scoreBuckets[similarity] += 1
            worst = max(scoreBuckets.values())
            if worst < min_worst:
                best = guess
                min_worst = worst
        
        return best