"""
https://www.acmicpc.net/problem/11557
- 테스트 케이스가 여러개 -> 술 소비 최대 학교 구하는 함수 만들기
- 입력받은 학교 정보를 튜플로 받아서 정렬해보자
"""

def max_school(school_num):
    list = []
    for i in range(school_num):
        school_name, school_alc = input().split()
        list.append((school_name, int(school_alc)))
    list.sort(key=lambda x: x[1], reverse=True)
    return list[0]


t = int(input()) # 테스트케이스

for _ in range(t):
    result = max_school(int(input()))
    print(result[0])
