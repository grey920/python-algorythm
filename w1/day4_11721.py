"""
https://www.acmicpc.net/problem/11721
BaekjoonOnlineJudge
->  BaekjoonOn
    lineJudge

"""


def solution(string: str):
    for i in range(0, len(string), 10): # 0부터 문자열 길이까지 10씩 증가하는 범위 -> 0, 10
        print(string[i:i + 10]) # 슬라이싱 사용해서 한 번에 10자씩 처리 (0~9, 10~19...) -> 메모리 사용 효율적


input_string = input()
solution(input_string)
