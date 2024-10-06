class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(0, len(tokens)):
            if tokens[i] in ["+","-","*","/"]:
                res = 0
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                if tokens[i] == "+":
                    res = first_num + second_num
                elif tokens[i] == "-":
                    res = first_num - second_num
                elif tokens[i] == "*":
                    res = first_num * second_num
                else:
                    res = first_num/second_num
                stack.append(res)
            else:
                stack.append(tokens[i])
        return int(stack[0])

        