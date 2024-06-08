"""
https://www.acmicpc.net/problem/2805

"""
n, m = map(int, input().split())  # n: 나무의 수, m: 필요한 나무 길이
trees = list(map(int, input().split()))

# 변수 초기화
low, high = 0, max(trees)


# 얻을 수 있는 나무의 총 길이 계산
def get_wood(cut_height):
    total = 0
    for tree in trees:
        if tree > cut_height:
            total += tree - cut_height
    return total


# 이진 탐색 시작
result = 0
while low <= high:
    mid = (low + high) // 2 # 중간값 계산
    wood = get_wood(mid) # 현재 절단 높이에서 얻을 수 있는 나무의 총 길이

    if wood >= m:
        result = mid # 현재에서 필요한 나무를 얻을 수 있다면 -> 결과 갱신
        low = mid + 1 # 절단 높이를 현재보다 더 높이 설정해도 되는지 확인
    else:
        high = mid - 1 # 얻을 수 있는 나무가 부족 -> 절단 높이를 낮춘다


print(result)

