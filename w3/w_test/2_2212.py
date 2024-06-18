"""
https://www.acmicpc.net/problem/2212
- 각 집중국의 수신 가능영역 거리의 최소값을 구한다 == 센서 사이가 가장 먼 곳에 집중국을 설치해야함
"""


def solution():
    n = int(input())
    k = int(input())
    sensors = list(map(int, input().split()))
    sensors.sort() # 센서 좌표 오름차순 정렬

    # 집중국이 센서수보다 많거나 같으면? -> 바로 수신됨 0
    if k >= n:
        return 0

    # 센서간 거리 구하기
    dist = []
    for i in range(1, n):
        dist.append(sensors[i] - sensors[i-1])

    # 가장 먼 거리부터 집중국 세우기 (k-1번 나누면 k개 집중국 설치됨)
    dist.sort(reverse=True) # 거리 내림차순 정렬
    for _ in range(k-1):
        dist.pop(0)
    return sum(dist)


print(solution())