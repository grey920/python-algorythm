"""
[접근방법]
- 중간을 기준으로 위/아래로 반을 나눈다
- 각 라인마다 -> 별을 연달아 출력 + 공백 계산해서 출력 + 별 출력
"""
n = int(input())

# 맨 위부터 중간까지
for i in range(1, n + 1):
    # 별: i개만큼 연달아 출력
    stars = '*' * i
    # 공백: 공백도 갯수를 계산하여 연달아 출력 (예. n = 5일때 i가 1이면, 양쪽의 별을 제외하고 공백은 8개)
    spaces = ' ' * (2 * n - 2 * i)
    # 🌟 양 끝에 별을 출력하고 가운데 공백을 출력한다
    print(stars + spaces + stars)

# 중간 아랫줄부터 끝까지
for i in range(n - 1, 0, -1): # 0까지 역순으로 반복
    stars = '*' * i
    spaces = ' ' * (2 * n - 2 * i)
    print(stars + spaces + stars)
