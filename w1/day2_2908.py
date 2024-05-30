"""
[문제분석]
- 숫자를 reverse 뒤집어서 비교한다.
-> 어떻게 뒤집을까?
    - slice 이용하기
    - 반복문 돌리기
    - 리스트의 reverse 이용하기
"""


# 함수1. 뒤집은 숫자를 반환하는 함수
def reverse_number(input_str):
    return int(input_str[::-1])


# 사용자로부터 입력받기
input_numbers = input().split()

# 더 큰 값을 max() 비교하기
first_reversed = reverse_number(input_numbers[0])
second_reversed = reverse_number(input_numbers[1])
print(max(first_reversed, second_reversed))
