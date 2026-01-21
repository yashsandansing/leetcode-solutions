class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create a hashmap to map single word index to words -> check word differences
        # if endWord not in WordList, return

        star_map = defaultdict(list)
        
        if endWord not in wordList:
            return 0

        for word in wordList:
            for ind in range(len(word)):
                key = word[:ind] + '*' + word[ind+1:]
                star_map[key].append(word)

        visited = set()
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)
        steps = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                for ind in range(len(curr)):
                    key = curr[:ind] + '*' + curr[ind+1:]

                    for value in star_map[key]:
                        if value == endWord:
                            return steps + 1
                        if value not in visited:
                            q.append(value)
                            visited.add(value)

            steps += 1
        return 0