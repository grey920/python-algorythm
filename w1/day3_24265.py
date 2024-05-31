"""
[문제분석]
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

"""

n = int(input())
total = 0

for i in range(1, n):
    for j in range(i + 1, n + 1):
        total += 1
print(total)

print("==================")
# 1 ~ n-1 까지 합
print(sum([i for i in range(1, n)]))

print("==================")
print(int(n * (n - 1) / 2))
