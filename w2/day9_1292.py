"""
https://www.acmicpc.net/problem/1292
"""
start, end = map(int,input().split())
list = []
cnt = 0
for i in range(end+1):
    nums = []
    for j in range(i):
        cnt += 1
        nums.append(cnt)
    list.append(nums)

# 찾기
total = 0
for i in range(len(list)):
    # print(f'i= {i}, list[i]={list[i]}')
    """
    i= 0, list[i]=[]
    i= 1, list[i]=[1]
    i= 2, list[i]=[2, 3]
    i= 3, list[i]=[4, 5, 6]
    i= 4, list[i]=[7, 8, 9, 10]
    i= 5, list[i]=[11, 12, 13, 14, 15]
    i= 6, list[i]=[16, 17, 18, 19, 20, 21]
    """
    for j in list[i]:
        if start <= j <= end:
            total += i
print(total)
