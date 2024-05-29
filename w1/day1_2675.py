# # 테스트 케이스 갯수 -> t번 반복
# t = int(input())
#
# # t번만큼 입력값 받고 출력 수행
# for i in range(t):
#     r, s = input().split()
#     # 문자열 s를 하나씩 순회하며 r만큼 반복 출력한다.
#     for a in s:
#         print(a * int(r), end="")
#     print()

"""
ChatGPT 코드 : List Comprehension과 join() 함수를 사용해서
"""
# 테스트 케이스 갯수 -> t번 반복
t = int(input())

# t번만큼 입력값 받고 출력 수행
for i in range(t):
    r, s = input().split()
    r = int(r)
    result = ''.join([char * r for char in s])  # 문자열 s의 각 문자를 r번 반복한 문자열을 생성
    print(result)  # 결과 출력