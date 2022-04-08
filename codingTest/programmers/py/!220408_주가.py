# https://programmers.co.kr/learn/courses/30/lessons/42584

# 1st try => 이게 되네..?
def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        temp = prices[i]
        count = 1
        idx = i+1
        while idx < len(prices)-1 and temp <= prices[idx]:
            count += 1
            idx += 1
        answer.append(count)
    
    return answer + [0]
