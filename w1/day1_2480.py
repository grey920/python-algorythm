"""
조건 분석 : 주사위의 값을 각각 A, B, C라 할 때
- A = B = C ➡️ 10,000 + prize * 1,000
- ( A = B )  or ( A = C ) or ( B = C ) ➡️  1,000 + prize * 100
- A != B != C  ➡️ 맥스값 * 100
"""

a, b, c = map(int, input().split())

# (다른 경우의 수를 빠르게 넘길 수 있도록) 모든 수가 같은 경우를 제일 먼저 확인한다
if a == b == c:
    prize = a * 1000 + 10000
# 주의: ( A = B )  or ( A = C ) or ( B = C ) 조건에서 a와 다른 수와 같은 경우 / a 제외한 두 수가 같은 경우를 분리하여 체크
elif a == b or a == c:
    prize = a * 100 + 1000
elif b == c:
    prize = b * 100 + 1000
# 모두 다르면 가장 큰 값을 기준으로 계산
else:
    prize = max(a, b, c) * 100

print(prize)

