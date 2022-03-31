# https://programmers.co.kr/learn/courses/30/lessons/12911#

# 1st try => 성공
# 만족스러운 코드인 것 같아! ^O^

def solution(n):
    num = bin(n)[2:]
    # num = format(n, 'b')
    
    one = num.count('1')
    level = len(num)
    
    idx = num.rfind('01')
    # 자릿수가 늘어나는 경우
    if idx == -1:
        answer = '10' + '0'*(level-one) + '1'*(one-1)
    # 자릿수 변경 없이 그 안에서 1/0 스위치되는 경우
    else:
        answer = num[:idx] + '10' + ''.join(sorted(num[idx+2:]))
        
    return int(answer, 2)
