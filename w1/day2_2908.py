"""
[문제분석]
- 소문자로 일괄 변경
- 한 문자씩 순회하면서 딕셔너리에 넣는다
- 순회가 끝나면, 값이 가장 큰 문자를 꺼낸다
- 가장 큰 값의 갯수를 체크해서 여러개라면 ? 를 출력한다
"""
from collections import Counter


# 문자열을 받아 가장 많이 나온 문자를 반환한다
def most_frequent_char(input_str):
    # 소문자로 변환
    lower_str = input_str.lower()

    # 문자의 빈도수 계산 ( Counter의 시간복잡도는 O(n) )
    counter = Counter(lower_str)

    # 가장 많이 나온 값의 빈도수 (max()함수의 시간복잡도 O(n))
    max_count = max(counter.values())

    # max_count로 가장 많은 문자 리스트 생성 (list comprehension의 시간복잡도 O(n))
    max_char = [char for char, cnt in counter.items() if cnt == max_count]

    # 가장 많은 문자가 여러개면 ? / 하나면 해당 문자를 출력
    return '?' if len(max_char) > 1 else max_char[0]


# 사용자로부터 입력 받기
input_str = input()

# 결과 출력
print(most_frequent_char(input_str))
