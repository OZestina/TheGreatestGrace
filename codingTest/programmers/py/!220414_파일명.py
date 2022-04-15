# https://programmers.co.kr/learn/courses/30/lessons/17686
#220414_파일명.py

# 1st try => 성공
# 1) 정규식 기억 안나서 다시 제대로 보고 옴 (식 작성 및 적용)
# 2) sorted()할 때 조건 2개 주는 부분 및 함수로 전달하는 법 다시 봄
import re

def solution(files):
    # p = re.compile('(\D+)(\d+)(.*)')
    p = re.compile('([a-zA-Z-. ]+)([0-9]+)(.*)')
    
    answer = []
    refile = []
    
    for file in files:
        refile += p.findall(file)
        
    lsts = sorted(refile, key = lambda x: (x[0].lower(), int(x[1])))
    
    for lst in lsts:
        answer.append(lst[0]+lst[1]+lst[2])
    
    return answer
