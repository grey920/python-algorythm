"""
- for문이 3개 => O(n^3)

[시간초과 코드]
# for i in range(1, n-1):
#     for j in range(i+1, n):
#         for k in range(j+1, n+1):
            # print(i, j, k)
            # total += 1

# print(total)
# print(3)

[접근 방법]
1. 일단 기존 3중 반복문에서 i, j, k를 출력해본다
2. 규칙을 찾아보자
3. 규칙을 토대로 다시 코드를 짠다

"""

n = int(input())
total = 0

"""1부터 n-2까지 반복하면서 등차수열의 합을 누적"""
for i in range(1, n-1):
    total += (i * (i+1) // 2)

print(total)
print(3) # O(n^3)