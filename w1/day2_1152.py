"""
[접근방법]
- 단어의 갯수를 카운트한다 -> 단어의 구분은 '공백;
- 즉, 문자열을 공백으로 나누어 리스트에 담고 길이를 구한다
"""
# 주어진 문자열에서 단어의 갯수를 세는 함수
def count_words(input_str):
    return len(input_str.split()) # 단어의 개수를 반환

# 사용자로부터 문자열 입력 받기
input_str = input()

# 단어의 갯수 출력
print(count_words(input_str))