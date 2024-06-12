"""
https://www.acmicpc.net/problem/1440
[조건]
- 모든 요소가 '00' -> 바로 0 리턴
- '시'의 조건 01 ~ 12를 벗어나면 -> 볼것도 없이 분 or 초
=> 백트래킹.. 되겠는데?
"""
time_arr = list(map(int, input().split(":")))
# print(time_arr)

def permute(nums):
    if sum(nums) == 0:
        return 0

    def backtrack(start, curr):
        # basecase
        if len(curr) == len(target):
            ans.append(curr[:])
            print(ans)
            return

        for i in range(start, len(target)):
            # 'h'인데 i가 0 이거나 13 이상인 경우 -> 넘어감
            # if target[i] == 'h' and (nums[start] == 0 or nums[start] >= 13):
            #     continue
            if target[i] not in curr:
                curr.append(target[i])
                backtrack(i+1, curr)
                curr.pop()
    ans = []
    target = ['h', 'm', 's']
    backtrack(start=0, curr=[])
    return len(ans)


print(permute(time_arr))