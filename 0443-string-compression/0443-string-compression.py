class Solution:
    def compress(self, chars: List[str]) -> int:
        # modify this in place
        # if a single letter of its kind -> dont add anything (only add when 2 or more)
        # if length >= 10 -> store in char + 1 and char + 2 indices
        
        # use a two pointer approach
        # r iterates over the elements collecting the number of elements
        # that are the same as the current substring
        # and accumulating the result
        # once it hits oob or a diff char, increment l and write down the numbers
        # till num == 0

        if len(chars) == 1:
            return 1

        l = r = 0

        while r < len(chars):

            curr_str = chars[r]
            curr_len = 0
            while r < len(chars) and chars[r] == curr_str:
                curr_len += 1
                r += 1

            chars[l] = curr_str
            l += 1
            if curr_len > 1:
                for i in str(curr_len):
                    chars[l] = i
                    l += 1

        return l
            