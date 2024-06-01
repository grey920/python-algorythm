import time

# 큰 리스트 생성
num_strings = 10000
strings = ['a'] * num_strings

# += 연산자를 사용한 문자열 결합
start_time = time.time()
result = ''
for s in strings:
    result += s
end_time = time.time()
print(f"+= 연산자를 사용한 결합 시간: {end_time - start_time}초")

# join() 메서드를 사용한 문자열 결합
start_time = time.time()
result = ''.join(strings)
end_time = time.time()
print(f"join() 메서드를 사용한 결합 시간: {end_time - start_time}초")

"""
[결과]
+= 연산자를 사용한 결합 시간: 0.0008699893951416016초
join() 메서드를 사용한 결합 시간: 4.792213439941406e-05초
"""