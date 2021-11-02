#https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3
#삼항연산자 자주 써보려고 노력중!

def solution(lottos, win_nums):
    zero = lottos.count(0)
    correct = 6-len(set(win_nums)-set(lottos))
    answer = [0,0]
    answer[0] = 7-(correct+zero) if correct+zero > 1 else 6
    answer[1] = 7-correct if correct > 1 else 6
    
    return answer



#다른 사람 풀이 보고 배우기
#등수를 배열로 하면 if문 안쓰고도 할 수 있다..!
def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    zero = lottos.count(0)
    correct = 6-len(set(win_nums)-set(lottos))
    
    #최대 맞은 수, 최소 맞은 수 [correct+zero, correct]
    answer = [rank[correct+zero], rank[correct]]
    return answer
