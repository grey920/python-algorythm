"""
[문제분석]
- 과일을 키, 과일의 갯수를 값으로 딕셔너리에 담아두고, 값 중에 5가 존재하는 경우 YES, 없으면 NO를 출력

1. 과일을 키로, 값은 모두 0으로 딕셔너리를 만든다
2. 첫 줄의 숫자만큼 반복해서 입력을 받는다.
3. 입력받은 문자열을 공백 기준으로 잘라서 첫번째 값인 과일을 찾아 두번째 값을 딕셔너리 값에 누적한다
4. 모든 입력이 끝난 후 딕셔너리의 값들 중 5가 존재하면 YES, 없으면 NO를 출력한다
"""
import sys

# 각 과일의 초기 개수 설정
fruit_counts = {
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0
}


def add_fruit_card(fruit_card):
    """과일 카드 정보를 딕셔너리에 추가하는 함수"""
    fruit, count = fruit_card.split()  # 공백 기준으로 과일과 개수 분리
    fruit_counts[fruit] += int(count)  # 해당 과일의 개수를 누적


def has_five_fruits():
    """과일 개수가 5개 이상인 과일이 있는지 확인하는 함수"""
    return 5 in fruit_counts.values()


# input()을 순회하여 받지 않고, 한번에 받아서 처리
input_cards = sys.stdin.read().strip().split('\n')
num_cards = int(input_cards[0])

# 각 카드 정보를 입력받아 처리
for card in input_cards[1:num_cards + 1]:
    add_fruit_card(card)

# 결과 출력
print("YES" if has_five_fruits() else "NO")