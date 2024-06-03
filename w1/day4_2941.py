"""
https://www.acmicpc.net/problem/2941
- 변경 리스트에 해당하는 문자들을 다 상관없는 문자로 (예. a) 변경하고 카운트한다?
"""


def count_croatian_letters(input_string):
    change_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

    for char in change_list:
        input_string = input_string.replace(char, 'A')
    return len(input_string)


input_string = input().strip()
print(count_croatian_letters(input_string))
