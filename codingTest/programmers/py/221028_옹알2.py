# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 옹알1 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120956

# 1st try
def solution(babbling):
    possible = ["ye", "ma", "aya", "woo"]
    answer = 0
    
    for bab in babbling:
        i = 0
        past = -1
        while i < len(bab):
            for j in range(4):
                if bab[i:].startswith(possible[j]) and past != j:
                    past = j
                    i += 2 + len(possible[j]) // 3
                    break
            else: break
        if i == len(bab): answer += 1
    return answer
