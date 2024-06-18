"""
https://leetcode.com/problems/climbing-stairs/
n = 40일 때
일반 재귀 : 12.074976205825806
DP Top-down 적용 후 : 5.0067901611328125e-05
DP Bottom-up 적용 후 : 9.059906005859375e-06
"""
import time
n = 40

# 재귀를 사용
def cs0(n):
    # 간단한 문제는 base case로 사용
    if n == 1:
        return 1
    if n == 2:
        return 2
    return cs0(n - 1) + cs0(n - 2)

start0 = time.time()
print(cs0(n))
print(f'일반 재귀 : {time.time() - start0}')


memo = {}
# Top-down > 재귀를 사용
def cs1(n):
    # 간단한 문제는 base case로 사용
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs1(n - 1) + cs1(n - 2)
    return memo[n]


start1 = time.time()
print(cs1(n))
print(f'DP Top-down 적용 후 : {time.time() - start1}')


# Bottom-up > 반복문
dp_table = {1: 1, 2: 2}
def cs2(n):
   for i in range(3, n+1):
       dp_table[i] = dp_table[i-1] + dp_table[i-2]

   return dp_table[n]
start2 = time.time()
print(cs2(n))
print(f'DP Bottom-up 적용 후 : {time.time() - start2}')
