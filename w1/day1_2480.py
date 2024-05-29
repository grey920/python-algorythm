"""
조건 분석 : 주사위의 값을 각각 A, B, C라 할 때
- A = B = C ➡️ 10,000 + n * 1,000
- ( A = B )  or ( A = C ) or ( B = C ) ➡️  1,000 + n * 100
- A != B != C  ➡️ 맥스값 * 100
"""

a, b, c = map(int, input().split())
n = 0

if a == b == c:
    n = a * 1000 + 10000
elif a == b or a == c:
    n = a * 100 + 1000
elif b == c:
    n = b * 100 + 1000
else:
    n = max(a, b, c) * 100

print(n)

