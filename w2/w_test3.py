"""
[스카이라인 쉬운거]
https://www.acmicpc.net/problem/1863

"""
n = int(input())
buildings = [list(map(int, input().split())) for _ in range(n)]
buildings.sort() # [[1, 1], [2, 2], [5, 1], [6, 3], [8, 1], [11, 0], [15, 2], [17, 3], [20, 2], [22, 1]]
ans = 0 # 최소 건물 개수
stack = []
for x, y in buildings:
    if y == 0: # 스카이라인 높이가 0 -> 빌딩이 사라질 때
        ans += len(stack) # stack에 남아있는 빌딩들은 모두 하나의 빌딩으로 처리
        stack = [] # stack 비워주고 다음 빌딩으로 넘어감
        continue

    while stack and stack[-1] > y: # stack이 비어있지 않고 && stack의 top이 y보다 클 때
        stack.pop() # stack 의 top을 pop
        ans += 1 # 스카이라인의 높이가 변하므로 ans 에 1 누적
    if not stack or stack[-1] < y: # stack이 비어있거나, stack의 top이 y보다 작을 때
        stack.append(y)
print(ans + len(stack)) # stack에 남아있는 빌딩들은 하나의 빌딩으로 처리
