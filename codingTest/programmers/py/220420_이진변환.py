# https://programmers.co.kr/learn/courses/30/lessons/70129

# 1st try -> 성공
def solution(s):
    zero = 0
    times = 0

    while len(s) > 1:
        temp = len(s)
        s = s.replace('0', '')
        length = len(s)
        zero += temp - length
        times += 1
        s = format(length, 'b')
        
    return [times, zero]
  
  
# 2nd try : 다른 사람의 풀이
# 1) while s != '1' => 굳이 len(s)로 할 필요가 없었다
# 2) length = s.count('1'), length를 바로 2진수 변환해 s에 대입 => 1만 세면 됐던것..!
def solution(s):
    times = zero = 0
    while s != '1':
        length = s.count('1')
        zero += len(s) - length
        times += 1
        s = format(length, 'b')
        
    return [times, zero]
