"""
https://www.acmicpc.net/problem/11899
[문제접근]
스택을 만들고 괄호를 담는다. 규칙에 따라 pop 한다
규칙
- ( 가 들어오면 스택에 push
- ) 가 들어오면
	- 스택의 마지막 괄호가 ( ➡️ pop
	- 스택의 마지막 괄호가 ) ➡️ push
모든 순회가 끝나고 남아있는 괄호의 갯수를 센다
"""
lists = input()
stack = []

for x in lists:
    if not stack:
        stack.append(x)
    elif x == ')' and stack[-1] == '(':
        stack.pop()
    else:
        stack.append(x)

print(len(stack))
