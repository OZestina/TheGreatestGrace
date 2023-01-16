# https://programmers.co.kr/learn/courses/30/lessons/17686
#220414_파일명.py

# 1st try => 성공
# 1) 정규식 기억 안나서 다시 제대로 보고 옴 (식 작성 및 적용)
# 2) sorted()할 때 조건 2개 주는 부분 및 함수로 전달하는 법 다시 봄
# 3) line 12 숫자 최대 길이가 5자여서 그 부분 추가해줬다 (23.01.16)
import re

def solution(files):
    # p = re.compile('(\D+)(\d+)(.*)')
    p = re.compile('([a-zA-Z-. ]+)([0-9]{1,5})(.*)')
    
    answer = []
    refile = []
    
    for file in files:
        refile += p.findall(file)
        
    lsts = sorted(refile, key = lambda x: (x[0].lower(), int(x[1])))
    
    for lst in lsts:
        answer.append(lst[0]+lst[1]+lst[2])
    
    return answer


# 2nd try (다른 사람의 풀이)(23.01.16)
# 그냥 정렬을 하는 방법도 있구나. 멋진 파이썬
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d{1,5}', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    
    return b
