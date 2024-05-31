"""
[문제분석]
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}

MenOfPassion 알고리즘은 입력받은 n만큼 반복을 수행하므로
시간복잡도 O(n)을 갖는다. 따라서 최고 차항은 늘 1이다.
"""

num = int(input())

print(num)
print(1)