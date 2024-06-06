"""
https://www.acmicpc.net/problem/27160
"""
import sys


def solution():
    inputs = sys.stdin.readline
    N = int(inputs().rstrip())

    # 카드 정보를 담을 딕셔너리 생성
    card_dict = {}

    # 딕셔너리에 카드 정보 셋팅 O(N)
    for _ in range(N):
        card_info = inputs().split()
        card_name = card_info[0]
        card_count = int(card_info[1])

        if card_name in card_dict: # 과일 이름이 이미 딕셔너리에 존재 -> 카드 카운트 누적
            card_dict[card_name] += card_count
        else: # 딕셔너리에 없는 과일 카드라면 -> 딕셔너리에 추가
            card_dict[card_name] = card_count

    # 카드 카운트가 5인 값이 딕셔너리에 존재하는지 확인 O(5) -> O(1)이겠지..?
    for count in card_dict.values():
        if count == 5:
            return "YES"
    return "NO"


result = solution()
print(result)
