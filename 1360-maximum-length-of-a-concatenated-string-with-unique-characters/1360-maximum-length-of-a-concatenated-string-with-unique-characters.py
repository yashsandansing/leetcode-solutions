class Solution:
    def maxLength(self, arr: List[str]) -> int:
        curr_set = set()
        def backtrack(ind):
            if ind == len(arr):
                return len(curr_set)
            res = 0
            if not self.overlap(curr_set, arr[ind]):
                for char in arr[ind]:
                    curr_set.add(char)
                res = backtrack(ind + 1)
                for char in arr[ind]:
                    curr_set.remove(char)
            return max(res, backtrack(ind + 1))

        return backtrack(0)


    def overlap(self, char_set, word) -> bool:
        hashmap = Counter(char_set) + Counter(word)
        return max(hashmap.values()) > 1