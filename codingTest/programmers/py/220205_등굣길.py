# https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3#

# 최단경로의 개수를 (큰수)로 나눈 나머지를 리턴하라고 하는 것을 못봐서 한동안 고민했었다...
# 문제를 잘 읽읍시다!!!
def solution(m, n, puddles):
    ways = []
    for i in range(n):
        ways.append([None]*m)
    ways[0][0] = 1
    
    for puddle in puddles:
        ways[puddle[1]-1][puddle[0]-1] = 0
    
    for i in range(n):
        for j in range(m):
            if ways[i][j] == None:
                ways[i][j] = 0
                if i > 0:
                    ways[i][j] += ways[i-1][j]
                if j > 0:
                    ways[i][j] += ways[i][j-1]
    answer = ways[n-1][m-1] % 1000000007
    
    return answer
