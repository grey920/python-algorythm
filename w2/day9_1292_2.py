"""
세그먼트 트리.. 시도하다가 너무 어려워서 포기..ㅎ
"""


def generate_sequence(end):
    # 숫자 리스트
    sequence = []
    num = 1
    while len(sequence) < end: # 문제에 주어진 끝 값까지만 수열 생성
        sequence.extend([num] * num)
        num += 1
        # print(sequence)
    return sequence


start, end = map(int, input().split())
sequence_list = generate_sequence(end)
max_num = 5
sub_sum = sum(sequence_list[start - 1:end])
print(sub_sum)
