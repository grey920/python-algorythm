"""
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

"""
n = int(input()) # 수열 길이
num_list = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i): # i 이전의 값들을 비교
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(max(dp))
