import sys

def male_switch_logic(switch, num):
    for i in range(num - 1, len(switch), num):
        switch[i] = 1 if switch[i] == 0 else 0
    return switch

def female_switch_logic(switch, num):
    num -= 1  # 1-based index를 0-based index로 변환
    left_i, right_i = num, num

    # 경계 체크 추가
    if left_i > 0 and right_i < len(switch) - 1 and switch[left_i - 1] != switch[right_i + 1]:
        switch[num] = 1 if switch[num] == 0 else 0
        return switch

    # 좌우 대칭을 유지하면서 가장 큰 범위 찾기
    while left_i > 0 and right_i < len(switch) - 1 and switch[left_i - 1] == switch[right_i + 1]:
        left_i -= 1
        right_i += 1

    # 범위 내의 스위치 상태 변경
    for i in range(left_i, right_i + 1):
        switch[i] = 1 if switch[i] == 0 else 0
    return switch

def print_switch_state(switch_state):
    for i in range(0, len(switch_state), 20):
        print(' '.join(map(str, switch_state[i:i + 20])))

def main():
    # 스위치 갯수
    switch_num = int(sys.stdin.readline().strip())
    # 각 스위치 상태
    switch_state = list(map(int, sys.stdin.readline().strip().split()))
    # 학생 수
    student_num = int(sys.stdin.readline().strip())
    # 학생 성별, 받은 수 배열
    students = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(student_num)]

    # 학생 순번대로 switch_state 변경
    for gender, num in students:
        if gender == 1:
            male_switch_logic(switch_state, num)
        else:
            female_switch_logic(switch_state, num)

    # 결과 출력
    print_switch_state(switch_state)

if __name__ == "__main__":
    main()
