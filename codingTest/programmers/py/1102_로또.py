#https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
#삼항연산자 자주 써보려고 노력중!

def solution(lottos, win_nums):
    zero = lottos.count(0)
    correct = 6-len(set(win_nums)-set(lottos))
    answer = [0,0]
    answer[0] = 7-(correct+zero) if correct+zero > 1 else 6
    answer[1] = 7-correct if correct > 1 else 6
    
    return answer
