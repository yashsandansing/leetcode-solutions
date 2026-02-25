class Solution:
    def calculate(self, s: str) -> int:
        # going to store all
        stack = []
        num = 0
        op = "+"
        n = len(s)
        for idx in range(n):
            char = s[idx]
            
            if "0" <= char <= "9":
                num = num * 10 + int(char)
            
            if char in "/-+*" or idx == n - 1:

                if op == "+":
                    stack.append(num)
                
                elif op == "-":
                    stack.append(-num)
                
                elif op == "*":
                    stack.append(num * stack.pop())
                
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                
                op = char
                num = 0

        return sum(stack)