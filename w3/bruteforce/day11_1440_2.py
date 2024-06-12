"""
https://www.acmicpc.net/problem/1440
[조건]
- 모든 요소가 '00' -> 바로 0 리턴
- '시'의 조건 01 ~ 12를 벗어나면 -> 볼것도 없이 분 or 초
=> 백트래킹.. 되겠는데?
"""
time_arr = list(map(int, input().split(":")))
hour = [h for h in range(1, 13)]
min_sec = [ms for ms in range(0, 60)]
count = 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
                if time_arr[i] in hour and time_arr[j] in min_sec and time_arr[k] in min_sec:
                    count += 1

print(count)

