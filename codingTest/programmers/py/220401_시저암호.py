# https://programmers.co.kr/learn/courses/30/lessons/12926

# 1st try => 성공
# 소문자 > 대문자 > 공백 순으로 값이 작아지기 때문에 if문에서는 큰 수부터 차례대로 비교할 수 있도록 함
# (그래서 if 97 <= alpha "and alpha <= 122" 부분 생략 가능)
def solution(s, n):
    answer = ''
    for letter in s:
        alpha = ord(letter)
        #대문자 65~90 소문자 97~122
        if 97 <= alpha:
            if (alpha+n) > 122:
                alpha -= 26
            answer += chr(alpha + n)
        elif 65 <= alpha:
            if (alpha+n) > 90:
                alpha -= 26
            answer += chr(alpha + n)
        else: answer += ' '
    return answer
  
  
  
# 2nd try (다른 사람의 풀이)
# 1) 문자도 부등호로 값 비교 가능하다! (ord() 사용 없이 바로 진행)
# 2) 벗어나는 수를 나머지수로 처리해서 (알파벳은 26자씩 반복되니까) 진행

def solution(s, n):
    answer = ''
    
    for letter in s:
        if 'a' <= letter:
            answer += chr((ord(letter) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= letter:
            answer += chr((ord(letter) - ord('A') + n) % 26 + ord('A'))
        else: answer += ' '
        
    return answer
