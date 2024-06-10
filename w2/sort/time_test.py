"""
4번 문제(https://www.acmicpc.net/problem/11899). 성능비교

"""
import time
bracketStr = input()
start_time = time.time()
while '()' in bracketStr:
    bracketStr = bracketStr.replace('()', '')
print(len(bracketStr))
end_time = time.time()
print(f'걸린시간={end_time - start_time}')
# T1 = 걸린시간=8.893013000488281e-05
# T2 = 걸린시간=5.507469177246094e-05
# T3 = 걸린시간=4.887580871582031e-05
# T4 = 걸린시간=0.00010013580322265625
########################################
import time

lists = input()

start_time = time.time()
stack = []

for x in lists:
    if not stack:
        stack.append(x)
    elif x == ')' and stack[-1] == '(':
        stack.pop()
    else:
        stack.append(x)
print(len(stack))
end_time = time.time()
print(f'걸린시간={end_time - start_time}')
# T1 = 걸린시간=0.00011897087097167969
# T2 = 걸린시간=8.296966552734375e-05
# T3 = 걸린시간=6.890296936035156e-05
# T4 = 걸린시간=8.296966552734375e-05
