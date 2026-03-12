class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # len candidates -> 1 to 100
        # candidates[i] -> positive
        result = list()
        curr_list = list()
        def backtrack(idx: int, curr_sum: int) -> None:
            if idx > len(candidates):
                return
            if curr_sum == target:
                result.append(curr_list.copy())
                return

            for i in range(idx, len(candidates)):
                if curr_sum + candidates[i] > target:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                curr_list.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i])
                curr_list.pop()
        
        candidates.sort()
        backtrack(0, 0)
        return result