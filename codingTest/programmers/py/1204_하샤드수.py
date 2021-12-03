# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    numSum = 0
    for n in str(x):
        numSum += int(n)
        
    if x % numSum == 0:
        return True
    else:
        return False
