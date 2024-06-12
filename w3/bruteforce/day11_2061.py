"""
https://www.acmicpc.net/problem/2061
일단 인수를 구해보자..
[입력값]
143 11
143 12

[출력값]
GOOD
BAD 11
"""
k, l = map(int,input().split())

# k의 인수
flag = True # 다 돌았는지 체크할 플래그값
for i in range(2, l): # 2부터 l-1까지 완전탐색
    if k % i == 0:
        print(f'BAD {i}')
        flag = False
        break
if flag:
    print("GOOD")


