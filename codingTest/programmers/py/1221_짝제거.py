# https://programmers.co.kr/learn/courses/30/lessons/12973

#1st try
#슬라이싱으로 시도, 효율성테스트 실패
def solution(s):
    if len(s) % 2 == 1: return 0
    position = 1
    while position < len(s):
        if s[position] == s[position-1]:
            s = s[:position-1] + s[position+1:]
            if position > 1: position -= 1
        else: position += 1
        #print(f's:{s},position:{position}')
    if len(s) == 0: answer = 1
    else: answer = 0
    return answer
  
  
#2nd try
#문자열 replace를 없애 연산을 빠르게 했더니 통과
def solution(s):
    if len(s) % 2 == 1: return 0
    alphabet = []
    for letter in s:
        if len(alphabet) == 0:
            alphabet.append(letter)
        elif letter == alphabet[len(alphabet)-1]:
            alphabet.pop()
        else:
            alphabet.append(letter)
    if len(alphabet) > 0: return 0
    else: return 1
