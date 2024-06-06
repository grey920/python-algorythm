"""
코딩 테스트
1. https://www.acmicpc.net/problem/1244

- 성별과 받은 수에 따라 스위치 조작
- 남: 받은 수의 배수 번호의 스위치 on -> off / off -> on
- 여: 받은 수와 같은 번호 스위치를 중심으로 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간의 스위치를 모두 바꿈

[입력]
1) 스위치 갯수
2) 각 스위치 상태
3) 학생 수
4 ~ ) 한 학생의 성별, 받은 수

[출력]
- 20개씩 출력
- 스위치 사이 빈칸
"""
import sys


def male_switch_logic(switch, num):
    for i in range(num-1, len(switch), num):
        switch[i] = 1 if switch[i] == 0 else 0
    return switch


def female_switch_logic(switch, num):
    # num을 중심으로 앞뒤 값이 같으면 이동, 앞뒤값이 다르거나 끝에 도달하면 끝 -> 범위 값을 스위치
    num -= 1
    left_i, right_i = num, num

    # 범위 구하기
    while left_i > 0 and right_i < len(switch) - 1 and switch[left_i - 1] == switch[right_i + 1]:
        left_i -= 1
        right_i += 1
    # 스위치
    # print(f'left_i={left_i}, right_i+1={right_i+1}')
    for i in range(left_i, right_i+1):
        switch[i] = 1 if switch[i] == 0 else 0
    return switch


# 스위치 갯수
switch_num = int(sys.stdin.readline())
# 각 스위치 상태
switch_state = list(map(int, sys.stdin.readline().split()))
# 학생 수
student_num = int(sys.stdin.readline())
# 학생 성별, 받은 수 배열
students = []
for i in range(int(student_num)):
    students.append(list(map(int, sys.stdin.readline().split())))

# 학생 순번대로 switch_state 변경
for i in range(len(students)):
    gender = students[i][0]
    num = students[i][1]
    if gender == 1:
        male_switch_logic(switch_state, num)
    else:
        female_switch_logic(switch_state, num)

# print(' '.join(map(str, switch_state)))
# 20개씩 출력
for i in range(0, len(switch_state), 20):
    print(' '.join(map(str, switch_state[i:i + 20])))
