"""
00:00:00 -> 0
01:00:00 -> 2
01:12:23 -> 4
21:23:01 -> 2
01:02:03 -> 6
59:59:01 -> 2
01:01:59 -> 4

"""
Time = input()
time_list = Time.split(':')
time_list.sort()
# print(time_list)

count = 0
for i in range(3):
    if 1 <= int(time_list[i]) <= 12:
        count += 1

if count == 3:
    print(6)
elif count == 2:
    print(4)
elif count == 1:
    print(2)
else:
    print(0)