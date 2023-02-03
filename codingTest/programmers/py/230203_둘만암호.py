# https://school.programmers.co.kr/learn/courses/30/lessons/155652

# 1st try
def solution(s, skip, index):
    answer = ''
    
    
    new_skip = [1] * 26
    for i in skip:
        new_skip[ord(i) - 97] = 0
    
    for i in s:
        number = ord(i) - 97
        count = index
        while count:
            number = (number + 1) % 26
            count -= new_skip[number]
        answer += chr(number + 97)
    
    return answer
  
  
  
# 2nd try (다른 사람 풀이 참고)
# 빠진 글자를 제외하고 계산할 수 있도록 새로운 문자 리스트를 만들어서 진행 (10진수 -> 8진수 처럼)
def solution(s, skip, index):
    answer = ''

    new_dict = {}
    letter_ord = []
    idx = 0
    for i in range(26):
        if chr(i + 97) in skip:
            continue
        else:
            new_dict[chr(i + 97)] = idx
            idx += 1
            letter_ord.append(chr(i + 97))
    l = len(letter_ord)
    
    for i in s:
        answer += letter_ord[(new_dict[i] + index) % l]

    return answer
