# https://school.programmers.co.kr/learn/courses/30/lessons/42897

# 1st try (해설 봄)
def calculate(money, l):
    for i in range(2, l):
        money[i] = max(money[i-1], money[i-2] + money[i])
    return money[l-1]

def solution(money):
    answer = 0
    
    l = len(money)
    #ver1: 첫째값 선택
    money_1 = [0] + money[:l-1]
    value_1 = calculate(money_1, l)
    
    #ver2: 마지막값 선택 가능
    money_2 = [0] + money[1:]
    value_2 = calculate(money_2, l)
    
    return max(value_1, value_2)
