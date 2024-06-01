"""
https://www.acmicpc.net/problem/28432
[입력]
1. 기록 개수 N
2. N개의 기록 한 줄씩 -> ? 포함
3. 후보 단어 개수 M
4. M개의 후보 한 줄씩
=> ? 에 들어갈 후보 단어 찾아서 출력
[조건]
- 기록에 중복 있으면 X
- ? : ? 이전 단어의 끝 문자로 시작 && ? 다음 단어의 시작 문자로 끝
"""


def find_candidate(records, candidates):
    # 후보 조건 확인 1: 중복제거 (set으로 변환)
    unique_candidates = set(candidates) - set(records)

    # '?'가 기록에 없는 경우 처리
    if '?' not in records:
        return None

    # 후보 조건 확인 2
    target_index = records.index('?')

    pre_target_word = records[target_index - 1] if target_index > 0 else None
    post_target_word = records[target_index + 1] if target_index < len(records) - 1 else None

    for candidate in unique_candidates:
        # not pre_target_word 체크를 안하니까 런타임 에러 발생함
        if (pre_target_word is None or candidate.startswith(pre_target_word[-1])) and \
                (post_target_word is None or candidate.endswith(post_target_word[0])):
            return candidate


# 기록 리스트 생성
record_count = int(input())
record_list = [input().strip() for i in range(record_count)]

# 후보 리스트 생성
candidate_count = int(input())
candidate_list = [input().strip() for i in range(candidate_count)]

result = find_candidate(record_list, candidate_list)
print(result)
