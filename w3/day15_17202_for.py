def sum_ab(a, b):
    numbers = []
    for l, r in zip(a, b):
        numbers.append(int(l))
        numbers.append(int(r))
    return numbers

def solution():
    import sys
    input = sys.stdin.readline

    # 두 전화번호 입력 받기
    a = input().strip()
    b = input().strip()

    # 두 전화번호의 각 자리수를 더한 문자열 생성
    combined = sum_ab(a, b)

    # while 루프를 통해 두 자리 숫자가 될 때까지 처리
    while len(combined) > 2:
        new_combined = []
        for i in range(len(combined) - 1):
            sum_adj = int(combined[i]) + int(combined[i + 1])
            new_combined.append(str(sum_adj % 10))
        combined = new_combined

    return ''.join(combined)

print(solution())