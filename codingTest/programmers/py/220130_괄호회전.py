# https://programmers.co.kr/learn/courses/30/lessons/76502

# 1st try
# 괄호 closing을 확인하는 별도의 함수를 만들어서 사용, 합격!
def solution(s):
    answer = 0
    if len(s) % 2 == 1: return answer
    for i in range(len(s)):
        if closing(s[i:len(s)]+s[0:i]) == True:   # s[i:]+s[:i] 라고 써도 되네ㅎㅎ
            answer += 1
    return answer
  

def closing(s):
    q = []
    for i in s:
        if i == '(':
            q.append('(')
        elif i == '{':
            q.append('{')
        elif i == '[':
            q.append('[')
        else:
            if len(q) == 0: return False
            pair = q.pop()
            if i == ')':
                if pair == '(': continue
            elif i == '}':
                if pair == '{': continue
            else: # i == ']'
                if pair == '[': continue
            return False
    if len(q): return False           # return False if len(q) else True (37~38줄 줄일 수도 있다)
    else: return True
    
