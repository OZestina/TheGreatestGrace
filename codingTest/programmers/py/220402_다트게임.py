# https://programmers.co.kr/learn/courses/30/lessons/17682

# 1st try => 성공
def solution(dartResult):
    scores = [0,0,0,0]   #연산 편의를 위해 0번째 라운드 포함
    idx = 0             #라운드 idx
    
    result = dartResult.replace("S", " S ").replace("D", " D ").replace("T", " T ").replace("*", "* ").replace("#", "# ").split()
    
    for score in result:
        # 보너스 점수 계산 (S는 1배로 제외)
        if score == 'D': scores[idx] = scores[idx]**2
        elif score == 'T': scores[idx] = scores[idx]**3
        elif score == 'S': continue
        # 옵션 계산
        elif score == '*':
            scores[idx] *= 2
            scores[idx-1] *= 2
        elif score == '#': scores[idx] *= -1
        # 숫자 점수
        else:
            idx += 1
            scores[idx] = int(score)
    
    return sum(scores[1:])
  

    
    
# 2nd try: 다른 사람의 풀이 참고
# 1) result split 방법: '10'만 바꾸면 모두 한 글자인 점을 착용
# 2) 보너스 점수표를 딕셔너리로 만듦
def solution(dartResult):
    scores = [0,0,0,0]   #연산 편의를 위해 0번째 라운드 포함
    idx = 0             #라운드 idx
    
    # 10만 바꾸면 모두 한 글자!
    result = ['10' if i == 'k' else i for i in dartResult.replace("10", "k")]
    bonus = {'S':1, 'D':2, 'T':3}
    
    for score in result:
        # 보너스 점수 계산
        if score in bonus:
            scores[idx] = scores[idx]**bonus[score]
        # 옵션 계산
        elif score == '*':
            scores[idx] *= 2
            scores[idx-1] *= 2  #이거 if문 안걸고싶어서 scores 4칸으로 만듦ㅎ
        elif score == '#': scores[idx] *= -1
        # 숫자 점수
        else:
            idx += 1
            scores[idx] = int(score)
    
    return sum(scores[1:])
  
  
# 3nd try : 다른 사람의 풀이, 정규식 활용
import re

def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'':1, '*':2, '#': -1}
    
    #정규식
    p = re.compile('(\d+)([SDT])([#*]?)')
    scores = p.findall(dartResult)  #작성한 정규식 규칙에 맞는 결과를 튜플 묶음(리스트)으로 
    
    for i in range(len(scores)):
        if scores[i][2] == '*' and i > 0:
            scores[i-1] *= 2
        scores[i] = int(scores[i][0])**(bonus[scores[i][1]]) * option[scores[i][2]]
    
    return sum(scores)
