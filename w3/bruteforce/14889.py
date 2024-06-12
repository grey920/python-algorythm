"""
*itertools 라이브러리 활용하면 완전 탐색 빠르게 구현 가능
[입력]
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
"""
from itertools import combinations
n = int(input())
scoreboard = [list(map(int, input().split())) for _ in range(n)]
team_with_0s = list(combinations(range(1, n), n // 2 - 1)) # 0번 사람 + (n // 2 - 1)명으로 팀 구성
m = float('inf') # 무한대. 최솟값을 찾을 때 초기값으로 사용하면 편함
for team1 in team_with_0s:
    team1 = [0] + list(team1)
    team2 = list(set(range(n)) - set(team1)) # 2번째 팀은 1번째 팀에 속하지 않는 사람들로 구성
    score1 = 0
    score2 = 0
    for i in range(n // 2):
        for j in range(n // 2):
            score1 += scoreboard[team1[i]][team1[j]] # team1[i]번 사람과 team1[j]번 사람이 만났을때의 점수 더하기
            score2 += scoreboard[team2[i]][team2[j]] # 위와 같이 team2도 점수 구하기
    m = min(m, abs(score1 - score2)) # 절대값 함수 abs 사용하여 두 값의 차이 구함
print(m)
