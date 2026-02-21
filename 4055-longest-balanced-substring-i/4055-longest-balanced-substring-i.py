class Solution:
    def longestBalanced(self, s: str) -> int:
        # len -> 1 to 1k
        # only lowercase letters
        # brute force
        # nested loop:=> i => start counter. calculate if n - i + 1 > best
        # if not: continue
        # if yes: add to the counter. check if min ele amount == max ele amount
        # if yes, update best, 
        # continue

        best = 0
        n = len(s)
        for i in range(n):
            if n - i + 1 < best:
                break

            counter = [0] * 26
            unique = max_freq = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                counter[idx] += 1

                # it was just added
                if counter[idx] == 1:
                    unique += 1
                max_freq = max(max_freq, counter[idx])

                curr = j - i + 1

                if unique*max_freq == curr:
                    best = max(best, curr)

        return best
