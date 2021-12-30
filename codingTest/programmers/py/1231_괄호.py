# https://programmers.co.kr/learn/courses/30/lessons/12909

# 1st try
# 만족!
def solution(s):
    que = 0
    for parenthesis in s:
        if parenthesis == '(': que += 1
        else: que -= 1
        if que < 0:
            return False
    if que != 0: return False
    return True
  
  
# 다른 사람의 풀이를 보고 마지막 부분 수정
# 12-13줄을 한 que로 끝냄! >ㅠ<
def solution(s):
    que = 0
    for parenthesis in s:
        if parenthesis == '(': que += 1
        else: que -= 1
        if que < 0:
            return False
    return que == 0
