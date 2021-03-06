"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid.
That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class Solution:
    def evalRPN(self, s) -> int:
        st = []
        for i in s:
            if i.lstrip("-").isdigit():
                st.append(int(i))
            elif i in '+-/*':
                n1 = st.pop()
                n2 = st.pop()
                if i == '+':
                    st.append(n1+n2)
                    continue
                if i == '-':
                    st.append(n2-n1)
                    continue
                if i == '*':
                    st.append(n2*n1)
                    continue
                if i == '/':
                    st.append(int(n2/n1))
                    continue
        return st.pop()

    def evalRPN2(self, tokens) -> int:
        stack = []
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: int(x / y)}
        for val in tokens:
            if val in operators:
                # print (stack)
                y = int(stack.pop())
                x = int(stack.pop())

                result = operators[val](x, y)
                stack.append(result)
            else:
                stack.append(val)

        return stack.pop()

obj = Solution()
#print(obj.evalRPN(["4", "13", "5", "/", "+"]))
print(obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))