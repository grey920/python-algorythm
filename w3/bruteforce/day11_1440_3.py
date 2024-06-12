"""
https://www.acmicpc.net/problem/1440

00:00:00 -> 0
01:00:00 -> 2
01:12:23 -> 4
21:23:01 -> 2
01:02:03 -> 6
59:59:01 -> 2
01:01:59 -> 4
"""
from itertools import permutations


def is_valid_time(h, m, s):
    return 0 < h < 13 and 0 <= m < 60 and 0 <= s < 60


def count_valid_times(time_arr):
    count = 0
    for perm in permutations(time_arr): # 순열
        h, m, s = perm
        if is_valid_time(h, m, s):
            count += 1
    return count


time_arr = list(map(int, input().split(":")))
print(count_valid_times(time_arr))
