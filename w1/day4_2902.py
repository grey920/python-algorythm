"""
[문제분석]
- 하이픈을 기준으로 가장 앞 문자만 추출하여 하나의 문자열로 출력한다
"""
separated_name = input().split("-")
short_name = ''.join([name[0] for name in separated_name])
print(short_name)

