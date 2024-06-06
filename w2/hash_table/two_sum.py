"""
input: nums = {4, 1, 9, 7, 5, 3, 16}, target:14
output: True

[접근 방법]
- 시간복잡도를 줄이기 위해 메모리 사용하기(대표적으로 해시 테이블)
"""


def two_sum(nums, target):
    # 딕셔너리에 저장
    memo = {}
    for v in nums:
        memo[v] = True

    # target 찾기
    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
    return False


result = two_sum(nums=[4, 1, 9, 7], target=14)
print(result)
