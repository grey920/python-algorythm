"""
[슈퍼 마리오]
https://www.acmicpc.net/problem/2851
[입력]
- 10줄에 버섯 점수 (100 이하의 양의 정수)
- 버섯이 나온 순서대로 점수 획득
[출력]
- 마리오 점수
*순서대로 집는다
*중단하면 뒤의 점수는 포기
*받은 점수의 합을 최대한 100에 가깝게 만든다

[접근방법]
1. 누적합을 기록한다
2. 누적합이 100을 넘으면
    -> |100 - 해당값| 과 |100 - 이전값| 을 비교
3. 100과의 차이가 더 적은 값을 출력
4. 차이가 같다면 더 큰 값을 출력력"""
import sys

input = sys.stdin.readline


# 입력값 셋팅
def get_input():
    params = []
    for i in range(10):
        params.append(int(input().strip()))
    return params


# 현재의 누적값에서 100과의 차이 vs 이전까지의 누적값과 100까지의 차이 비교 -> 차이가 더 적은 누적값 리턴
def get_point_by_diff(curr_val, prev_val):
    curr_diff = abs(100 - curr_val)
    prev_diff = abs(100 - prev_val)
    if curr_diff < prev_diff:
        return curr_val
    elif curr_diff > prev_diff:
        return prev_val
    else:
        return max(curr_val, prev_val)


def solution(params):
    answer = 0
    pre_sum = 0
    # 누적
    for i in range(10):
        pre_sum += params[i]
        # 누적한 값이 100을 넘는 경우 -> 절대값 비교
        if pre_sum >= 100:
            answer = get_point_by_diff(pre_sum, pre_sum - params[i])
            break
    else: # 전부 돌아도 100이 안넘는 경우 -> 전체 합 리턴
        answer = pre_sum

    return answer


print(solution(get_input()))
