"""
한조
https://www.acmicpc.net/problem/14659
[입력]
7
6 4 10 2 5 7 11
[출력]
3
[접근방법]
순차적으로 돌면서 본인보다 높은 봉우리가 나오기 전까지 카운트 센다?
"""


def solution():
    n = int(input())
    peaks = list(map(int, input().split()))
    answer, count = 0, 0
    start = 0
    for end in range(1, n):
        if peaks[start] < peaks[end]: # 더 높은 봉우리를 만나는 경우
            answer = max(answer, count) # 최대값 설정
            start = end # 위치 재설정
            count = 0 # 카운트 초기화
        else:
            count += 1
    answer = max(answer, count)
    return answer


print(solution())