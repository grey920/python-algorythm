"""
https://www.acmicpc.net/problem/1654
[입력]
4 11
802
743
457
539
"""
n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]

answer = 1 # 정답은 항상 1 이상
left = 1
right = 2 ** 31 - 1 # 문제에서 주어진 랜선의 최대 길이
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    print(f'mid={mid}, answer={answer}')
    for line in lines:
        cnt += line // mid # 랜선 길이로 나눈 몫이 만들 수 있는 랜선의 갯수. line보다 mid가 크면 계속 cnt는 0
        print(f'mid={mid}, line={line}, cnt={cnt}')
    if cnt >= k: # k개 이상의 랜선을 만들 수 있다면 정답 갱신
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
