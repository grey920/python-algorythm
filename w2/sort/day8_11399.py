"""
https://www.acmicpc.net/problem/11399
ATM
"""
def get_prefix_sum(n):
    prefix_sum = [0] * n # 누적합 저장할 배열 초기화
    prefix_sum[0] = atm_lines[0]
    for i in range(1, n): # 0번 인덱스는 미리 구했으므로 1번 인덱스부터 시작
        prefix_sum[i] = prefix_sum[i-1] + atm_lines[i]
    return prefix_sum


n = int(input())
atm_lines = list(map(int, input().split()))
atm_lines.sort()

prefix_sum = get_prefix_sum(n)
print(sum(prefix_sum))