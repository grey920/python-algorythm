"""
우유 축제
https://www.acmicpc.net/problem/14720
[입력]
7
0 1 2 0 1 2 0
[출력]
7
[접근방법]
0 -> 1 -> 2 -> 0 의 순서를 지켜야 한다.
=> 3으로 나눈 나머지와 같다!
"""


def solution():
    n = int(input())
    milk_st = list(map(int, input().split()))
    curr_milk = 0 # 마셔야 하는 순서의 우유
    answer = 0

    for milk in milk_st:
        if milk == curr_milk: # 마셔야할 순서의 우유라면 -> count+
            answer += 1
            curr_milk = (curr_milk + 1) % 3 # 다음 순서 : 0 1 2 0 1 2 ...

    return answer


print(solution())
