"""
https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3
"""

def solution(friends, gifts):
    size = len(friends)
    table = [[0]*size for _ in range(size)]
    gift_index = [0] * size

    # 친구 -> 인덱스로 변환
    index_map = {}
    for i in range(size):
        index_map[friends[i]] = i # {'muzi': 0, 'ryan': 1, 'frodo': 2, 'neo': 3}

    # 선물 테이블과 선물 지수 셋팅
    for gift in gifts:
        giver, receiver = gift.split()
        idx_giver = index_map[giver]
        idx_receiver = index_map[receiver]

        table[idx_giver][idx_receiver] += 1
        gift_index[idx_giver] += 1
        gift_index[idx_receiver] -= 1

    # 다음 달 선물 계산
    next_gift = [0] * size
    for i in range(size):
        for j in range(i+1, size):
            if table[i][j] > table[j][i]:
                next_gift[i] += 1
            elif table[i][j] < table[j][i]:
                next_gift[j] += 1
            else: # 선물지수로 계산
                if gift_index[i] > gift_index[j]:
                    next_gift[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_gift[j] += 1

    return max(next_gift)


result = solution(friends=["muzi", "ryan", "frodo", "neo"], gifts=["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
print(result)