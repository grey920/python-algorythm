"""
차집합을 이용한 중복 제거와 리스트 컴프리헨션으로 중복 제거의 성능 차이
"""
import time

# 테스트 데이터 생성
records = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
candidates = ["apple", "fig", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya"]

# 리스트 컴프리헨션을 사용한 중복 제거
start_time = time.time()
filtered_candidates_list = [x for x in candidates if x not in records]
end_time = time.time()
print(f"리스트 컴프리헨션 시간: {end_time - start_time}")
print(filtered_candidates_list)

# 집합을 사용한 차집합
start_time = time.time()
filtered_candidates_set = list(set(candidates) - set(records))
end_time = time.time()
print(f"집합 차집합 시간: {end_time - start_time}")
print(filtered_candidates_set)
