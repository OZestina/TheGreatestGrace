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
            answer[i] += 1
            if prices[i] > prices[j]:
                break
            
    return answer


# 3rd try (2022.07.21)
def solution(prices):
    answer = []
     = lenprices)
    for price in range(l)
        idx = 1
        count = 0
        while price + idx < l:
            if prices[price] > prices[price + idx]:
                count += 1
                break
            else:
                idx += 1
                count += 1
        answer.append(count)
    return answer
