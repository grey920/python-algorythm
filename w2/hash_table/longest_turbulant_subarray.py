"""
key in { } 가 핵심
input: nums={100, 4, 200, 1, 3, 2}
output: 4 ([1, 2, 3, 4])

[코드 설계]
- 인풋을 순회
-> 연속된 수 중 가장 작은 값인지 Hash Table의 키로 찾아본다 (해당 값의 -1 값이 키로 존재하는지)
-> 가장 작은 수일때만 다음 값이 Hash Table의 키로 존재하는지 O(1)로 찾아보고, 있으면 카운트를 1 더하며 반복한다.
"""
def longest_consecutive(nums):
    longest = 0
    num_dict = {}
    # 딕셔너리에 키 셋팅
    # for num in nums:
    #     num_dict[num] = True

    # 리스트 컴프리헨션을 이용해 한번에 생성
    num_dict = {x: x+1 for x in nums} # target을 누적할 필요 없이 num_dict[target]을 다음 타겟으로 바로 활용 가능

    # Hast Set 이용
    # num_set = set(nums)

    # 찾기
    for num in num_dict: # if 조건문 덕분에 O(N)이 걸림
        if num - 1 not in num_dict: # 이전 값이 딕셔너리에 존재하지 않으면 연속이 시작되는 수
            cnt = 1 # 연속된 횟수 카운트
            target = num + 1 # 연속된 값
            while target in num_dict: # 연속이 끝날때까지 반복 (위에 if 조건이 있기 때문에 while 반복은 기껏해야 한 번)
                target += 1
                cnt += 1
            # 연속이 끝났다면 연속된 최대값 갱신
            longest = max(longest, cnt)
    return longest


result = longest_consecutive([6, 7, 100, 5, 4, 4])
print(result)
