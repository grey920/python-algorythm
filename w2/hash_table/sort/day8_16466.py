"""
https://www.acmicpc.net/problem/16466
내가 확인한 규칙
- 시작이 1이 아니면 -> 1을 반환한다
- 1부터 연속하다 끊어지면 -> 끊어진 다음값을 반환한다
- 둘 다 아니면 -> 마지막의 다음값을 반환한다
"""
def find_2nd_ticket_num(arr):
    arr.sort() # 오름차순 정렬

    # 조건1) 시작이 1이 아니면 -> 1 반환
    if arr[0] != 1:
        return 1

    # 조건2) 연속하다 끊어지면 -> 끊어진 다음값 반환
    target = 1
    for num in arr:
        if num == target:
            target += 1
        else: # 끊어진 경우
            return target
    # 조건3) 둘 다 아니면 마지막의 다음값 반환
    return arr[len(arr)-1] + 1


n = int(input()) # 1차 티켓 수
tickets = list(map(int, input().split()))

result = find_2nd_ticket_num(tickets)
print(result)
