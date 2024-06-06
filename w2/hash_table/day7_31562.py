"""
https://www.acmicpc.net/problem/31562
[입력]
1) 음을 아는 노래 개수 N & 맞히기 시도할 노래 개수 M
2) N개줄 반복
    -> 노래 제목의 길이 T & 대소문자 노래 제목 S & 노래의 첫 일곱개 음이름 a1 ~ a7
3) N + 2번째 줄부터 M개 줄에 걸쳐 맞히기 시도할 노래의 첫 세 음이름 b1, b2, b3

*같은 제목은 두 번 이상 X (중복X)

[출력]
- 프로그램에 저장된 노래와 첫 세 음이 동일한 노래가 하나만 있으면 -> 노래 제목
- 두 개 이상이면 -> ?
- 없으면 -> !
한 줄에 하나씩 출력

[접근 방법]
- 크게 프로그램에 저장된 곡 / 맞출 곡 으로 나눠서 음 세개가 겹치는 곡을 찾아라~ 라는 것?
- 처음의 음 세 개가 겹치는 곡이 여러개일 수 있다 -> 음 세개를 키로 쓰고, 값으로 노래 제목을 리스트로 넣어볼까?
"""
import sys
from collections import defaultdict

def solution():
    inputs = sys.stdin.readline
    n, m = map(int, inputs().split())  # n: 아는 노래 개수, m: 맞출 노래 개수
    dict = defaultdict(list) # value를 리스트에 append()로 추가할 예정

    # defaultdict에 노래 저장
    for _ in range(n):
        song_data = inputs().split() # ['11', 'TwinkleStar', 'C', 'C', 'G', 'G', 'A', 'A', 'G']
        dict_key = ''.join(song_data[2:5])
        dict_value = song_data[1]
        dict[dict_key].append(dict_value)  # key: 첫 음 3개 / value: 노래 제목

    # 노래 찾기
    for _ in range(m):
        target_cord = ''.join(inputs().split()) # 맞힐 음 3개
        if target_cord not in dict: # key에 타겟 코드가 존재하는지 확인 O(1)
            print('!')
        else:
            if len(dict[target_cord]) == 1:
                print(dict[target_cord][0])
            else:
                print('?')


solution()
