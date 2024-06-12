"""
- 순열: 순서O
- 조합: 순서X
- 부분집합: 조합 응용

"""
import time
import itertools
# 순열. nums=[1, 2, 3, 4]로 만들 수 있는 모든 순열 반환하기
def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans


start = time.time()
print(permute(nums=[1, 2, 3, 4]))
end = time.time()
print(f'직접 구현 > 걸린시간: {end - start}') # 직접 구현 > 걸린시간: 3.719329833984375e-05

# itertools 사용
start2 = time.time()
result = []
for i in itertools.permutations([1, 2, 3, 4], 4):
    result.append(i)
print(result)
end2 = time.time()
print(f'itertools > 걸린시간: {end2 - start2}') # itertools > 걸린시간: 9.703636169433594e-05

