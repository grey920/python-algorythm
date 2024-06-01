# 첫 시도 -> 시간 초과!! -> 호출 횟수를 줄이자
# 재귀 함수가 호출되는 횟수는 피보나치 수와 일치한다 (n이 5이면, f(3) + f(4)인 5만큼 호출)
# 따라서, 저장된 값을 꺼내씀으로써 호출 횟수를 줄이고 n의 피보나치 수를 값으로 반환한다.
def fib(n):
    f[1] = 1
    f[2] = 1

    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


# 리스트에 저장해둔 값을 꺼내와 사용하기 때문에 호출 횟수가 n
# 문제에서 3부터 n까지 호출하는 부분을 카운트하므로 1과 2를 제외한 n-2번만 호출한다
def fibonacci(n):
    return n - 2


# 피보나치 수를 계산할 n을 입력받음
n = int(input().strip())

# 미리 값을 보관해 둘 리스트를 초기화해둔다 (메모이제이션)
f = [0] * (n + 1)

print(fib(n))
print(fibonacci(n))