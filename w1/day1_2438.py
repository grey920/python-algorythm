"""
오잉.. 의도치않게 역순 별찍기를 했네;;;;
이게 아닌데

num = int(input())
for i in range(0, num):
    for j in range(num-i, 0, -1):
        print("*", end="")
    print()
"""

"""
[문제분석]
- 사용개념 / 접근법 / 풀이방식
: 분류가 구현인 문제 -> 2중 반복문을 돌아 구현한다.
: 두번째 반복에서 1부터 N까지 점점 숫자가 커져야 한다.
-> 첫번째 반복 변수인 i과 N을 이용해서 j가 1부터 N까지 증가하도록 계산식을 세운다. (최대값인 N은 고정값이므로 i가 점점 작아져야 한다.)
"""
n = int(input())
#
# # 처음은 n과 i가 같으므로 + 1을 해야 별 한개부터 시작이 가능하다.
# for i in range(n, 0, -1):
#     for j in range(0, n-i+1):
#         print("*", end="")
#     print()


for i in range(1, n + 1): # 1 ~ n까지 반복
    print('*' * i) # *을 i번 반복해서 문자열 출력

