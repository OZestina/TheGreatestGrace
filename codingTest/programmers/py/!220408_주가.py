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


# 2nd try
# 그냥 이중for문도 통과되는 거였다...
def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]: answer[i] += 1
            else: 
                answer[i] += 1
                break
            
    return answer


# 3rd try
