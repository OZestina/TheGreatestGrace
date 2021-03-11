# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3#

#1st try
#되게 잘 썼다고 생각했는데, min()을 사용하면 더 간단해지는 것이었다!!!
def solution(nums):
    max_have = len(nums)/2
    pair = len(list(set(nums)))
    
    if pair >= max_have :
        answer = max_have
    else:
        answer = pair
        
    return answer
  
#2nd try
def solution(nums):
    max_have = len(nums)/2
    pair = len(set(nums))
    
    answer = min(max_have, pair)
    return answer
  
#마냑에 더 짧게 하고 싶다면!
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
