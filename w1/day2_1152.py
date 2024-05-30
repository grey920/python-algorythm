"""
[접근방법]
- 단어의 갯수를 카운트한다 -> 단어의 구분은 '공백;
- 즉, 문자열을 공백으로 나누어 리스트에 담고 길이를 구한다
"""
str = input()

def count_words( str ):
    # 공백 기준으로 split
    word_list = str.split()
    return len( word_list )

print(count_words(str))