"""
별자리가 될 수 있다면
https://www.acmicpc.net/problem/30821
[입력]
정N각형의 꼭짓점 개수 정수 N (5~100)
[출력]
정N각형의 꼭짓점을 이어 만들 수 있는 별의 개수
[문제 접근]
- N개의 꼭짓점 중 5개의 꼭짓점을 선택하는 조합을 찾아낸다.
- 순열은 안될까? -> 예시 그림으로 봤을 때 순서를 바꿔도 하나이므로 순열은 X
- 모듈을 쓰니 시간초과-> 배열 만들지말고 공식을 써야겠다
"""
import math
n = int(input())
k = 5


def solution(n):
    # 조합 구하는 공식
    answer = math.factorial(n) // math.factorial(n-k) // math.factorial(k)
    return answer


print(solution(n))



