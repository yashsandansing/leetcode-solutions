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
                visited.add(curr)

                if curr == endWord:
                    return steps
                # print('entering check condition for', curr)
                for ind in range(len(curr)):
                    key = curr[:ind] + '*' + curr[ind+1:]
                    # print('checking for', key, star_map[key])
                    for value in star_map[key]:
                        if value not in visited:
                            q.append(value)
                            visited.add(value)
                            
                # print('q status', list(q))
                # print('visited status', visited)
            steps += 1
        return steps if steps == endWord else 0