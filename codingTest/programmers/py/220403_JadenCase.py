# https://programmers.co.kr/learn/courses/30/lessons/12951

# 1st try => 성공!
# for문이 한 번만 돌아가는게 가장 시간이 적게 걸릴 것으로 판단
def solution(s):
    answer = ''
    flag = True
    
    for letter in s:
        if '0' <= letter and letter <= '9':
            flag = False
        elif letter == ' ':
            flag = True
        else:   #알파벳일 경우
            if flag == True:
                if 'a' <= letter and letter <= 'z':
                    letter = chr(ord(letter) - 32)
                flag = False
            else:
                if 'A' <= letter and letter <= 'Z':
                    letter = chr(ord(letter) + 32)
        answer += letter
    return answer
  
  
  
# 2nd try
# 코테를 통과하는 것은 아니지만 비슷한 내용의 함수가 있었다
# 이렇게 하면 시작하는 모든 알파벳이 대문자가 된다!
# 하지만: I'M The One / 3People Unfollowed Me 같은 리턴값이 나옴ㅎ
def solution(s):
  return s.title()

# 3rd try : 다른 사람의 풀이
# 첫글자에 상관없이 맨 첫번째 글자만 대문자로 바꿔주는 함수가 있었다: 스트링.capitalize()
# 공백이 두 칸일 경우 len이 0인게 생기는데, 슬라이싱으로 접근하면 index out of range 에러가 뜨지만, 이 capitalize() 함수로는 문제 없다 (에러처리한듯)
def solution(s):
  return ' '.join([word.capitalize() for word in s.split(" ")])
