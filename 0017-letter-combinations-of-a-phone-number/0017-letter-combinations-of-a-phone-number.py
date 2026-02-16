class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits -> 2 to 9
        # digits.len -> 1 to 4
        # in -> string
        # out -> list[string]

        # {"2": {"abc"}, "3": {"def"}}
        # len(curr) == 2: res.append(curr) return   <===
        # ind -> track position on digits   <=======
        # ind2 -> track position of letters wrt digits: 2:0 -> a, 2:1 - b
        # iterate over the lenght of your current digit:
            # 2 -> a, b, c
            # make_choice -> "a", ind+1
        
            # 3 -> d, e, f
            # make_choice -> "ad", ind+1 
            # undo_choice -> "a"

        dig2alpha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        
        def recursive(ind, curr):
            if ind == len(digits):
                res.append("".join(curr.copy()))
                return
                
            digit = digits[ind]
            for alpha in dig2alpha[digit]:
                curr.append(alpha)
                recursive(ind + 1, curr)
                curr.pop()
            
            return
        
        recursive(0, [])
        return res
        
