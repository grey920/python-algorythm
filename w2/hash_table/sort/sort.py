"""
https://www.acmicpc.net/problem/1181
- N개의 단어 -> 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬
- 중복은 제거
"""
import sys

inputs = sys.stdin.readline
n = int(inputs().rstrip())

word_list =[]
for i in range(n):
    word = str(inputs().rstrip())
    word_list.append((len(word), word)) # 튜플 형태로 (길이, 단어) 저장
word_list = list(set(word_list))
word_list.sort() # 튜플의 첫번재 값인 len으로 먼저 정렬 -> 두번째 값인 word로 알아서 정렬
for len, word in word_list:
    print(word)

######################################
n = int(input())
words = {input() for _ in range(n)} # 중복 제거를 위해 set 으로 생성
words = list(words) # 정렬을 위해 list 로 변환
words.sort(key=lambda x: (len(x), x)) # 길이 순으로 정렬, 길이가 같다면 사전 순으로 정렬
for word in words:
    print(word)