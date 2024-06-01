"""
https://www.acmicpc.net/problem/2745
[문제분석]
- 문제: 주어진 B진법 수 N을 10진법으로 변환하기
- int() 함수의 두번째 인자인 base 활용하기
"""


def solution(string: str):
    num, base = string.split()
    return int(num, int(base))


input_str = input()
print(solution(input_str))
