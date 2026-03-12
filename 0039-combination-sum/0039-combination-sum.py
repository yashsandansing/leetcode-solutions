class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()
        def backtrack(idx: int, remaining: int, curr_cand: List[int]):
            if remaining == 0:
                result.append(curr_cand.copy())
                return
            
            for i in range(idx, len(candidates)):
                if candidates[i] > remaining:
                    break
                curr_cand.append(candidates[i])
                backtrack(i, remaining - candidates[i], curr_cand)
                curr_cand.pop()

        backtrack(0, target, list())
        return result
