"""
핸드폰 번호 궁합
https://www.acmicpc.net/problem/17202
[입력]
74759336
36195974
[출력]
26

[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
[3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
[8, 2, 6, 0, 4, 8, 2, 6, 0, 4, 8, 2, 6]
[0, 8, 6, 4, 2, 0, 8, 6, 4, 2, 0, 8]
[8, 4, 0, 6, 2, 8, 4, 0, 6, 2, 8]
[2, 4, 6, 8, 0, 2, 4, 6, 8, 0]
[6, 0, 4, 8, 2, 6, 0, 4, 8]
[6, 4, 2, 0, 8, 6, 4, 2]
[0, 6, 2, 8, 4, 0, 6]
[6, 8, 0, 2, 4, 6]
[4, 8, 2, 6, 0]
[2, 0, 8, 6]
[2, 8, 4]
[0, 2]
"""


def sum_ab(a, b):
    numbers = []
    for l, r in zip(a, b):
        numbers.append(int(l))
        numbers.append(int(r))
    return numbers


def solution():
    a = list(input())
    b = list(input())
    numbers = sum_ab(a, b)
    memo = [[-1 for j in range(10)] for i in range(10)]

    def dp_solution(numbers):
        if len(numbers) == 2:  # base case
            return numbers

        new_numbers = []
        for i in range(len(numbers) - 1):
            l = numbers[i]
            r = numbers[i + 1]
            if memo[l][r] != -1:  # 메모리에 두 숫자의 합이 있으면 꺼내서 사용
                new_numbers.append(memo[l][r])
            else:  # 메모리에 두 숫자의 합이 없다면 -> 저장
                memo[l][r] = (l + r) % 10
                new_numbers.append(memo[l][r])
        print(new_numbers)
        return dp_solution(new_numbers)  # 새로 만들어진 문자열로 다시 덧셈 시작!

    answer = dp_solution(numbers)
    return str(answer[0])+str(answer[1])


print(solution())
