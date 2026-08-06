class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
                print(stack,1)
            elif t=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
                print(stack,2)

            elif t=='*':
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
                print(stack,3)

            elif t=='/':
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
                print(stack,4)

            else:
                stack.append(int(t))
                print(stack)


        return stack[0]