'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
'''

class Solution:
    def evalRPN(self, tokens):

        #function to check whether it is a number
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        #a stack to store the numbers
        st = []

        #Go through tokens
        for i in tokens:

            #if it is a operator
            if not is_integer(i):

                #take numbers from the stack and perform the operation
                sym = i
                n2 = st.pop()
                n1 = st.pop()

                if sym == "+":
                    val = n1 + n2
                elif sym == "-":
                    val = n1 - n2
                elif sym == "*":
                    val = n1 * n2
                else:
                    val = int(n1 / n2)

                st.append(val)

            #If it is a number append to the stack
            else:
                st.append(int(i))

        return st[0]



tokens =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens1 = ["4","13","+"]
print(Solution1().evalRPN(tokens))
