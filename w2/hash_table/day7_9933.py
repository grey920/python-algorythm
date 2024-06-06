"""
https://www.acmicpc.net/problem/9933
주어진 목록 중에 뒤집힌 문자열이 포함된 문자열이 존재하는지 확인
-> 있으면 해당 문자의 길이와 가운데 반환
-> 없으면 자기 자신이 회문인 문자열을 찾아 길이와 가운데 문자 반환
"""
from sys import stdin


def find_pwd():
    # dictionary 생성
    pwd_dict = {}
    # 딕셔너리에 입력받은 문자를 key로, 뒤집은 값을 value로 저장 O(N)
    for _ in range(N):
        pwd = inputs().rstrip()
        pwd_dict[pwd] = pwd[::-1]

    # 탐색 시작
    for pwd in pwd_dict:
        pwd_length = len(pwd)
        if pwd[::-1] in pwd_dict: # 입력받은 문자열을 뒤집은 문자열이 key로 있는지 확인 O(1)
            return [pwd_length, pwd[pwd_length // 2: pwd_length // 2 + 1]] # 있으면 길이와 가운데 문자 리턴
        else:
            if pwd is pwd_dict[pwd]: # 뒤집은 문자열이 key에 없는 경우 -> 스스로가 회문인 경우 -> 딕셔너리 키와 값이 동일
                return [pwd_length, pwd[pwd_length // 2: pwd_length // 2 + 1]]


inputs = stdin.readline
N = int(inputs().rstrip())
result = find_pwd()
print(*result) # 리스트로 받은 값을 언패킹
