# 딕셔너리 선언과 동시에 초기화
score = {
    'math': 97,
    'eng': 49,
    'kor': 89
}

print(score['math']) #97

score['math'] = 45 # 재할당
print(score['math']) #45

score['sci'] = 100
print(score['sci']) #100

# score['music'] # KeyError: 'music'
print('music' in score) # 키가 존재하는지 확인

if 'music' in score: # [중요] 시간복잡도O(1)으로 키의 존재여부를 알 수 있음!!!
    print(['music'])
else:
    score['music'] = 0
