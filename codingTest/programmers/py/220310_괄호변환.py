# https://programmers.co.kr/learn/courses/30/lessons/60058

# 1st try => success
# 왼/오를 l/r로 두 개 둘게 아니라 하나로 해서(아래에서는 c) 0과 비교하면 연산도 줄고 변수도 준다!
def solution(p):
    temp = ''
    loaf = []
    loaf_c = []
    correct = False
    c = 0
        
    for i in p:
        # 괄호 쌍 계산
        if i == '(': c -= 1
        else: c += 1
        # 올바른 괄호 여부 확인
        if c < 0:
            correct = True
        # 올바르지 않을 경우 반대로 저장
        if correct == True:
            temp += i
        else:
            if i == '(': temp += ')'
            else: temp += '('
        # 괄호 쌍이 맞았을 경우 처리
        if c == 0:
            if len(loaf) > 0 and correct == True and loaf_c[-1] == True:
                loaf[-1] += temp
            else:
                loaf.append(temp)
                loaf_c.append(correct)
            temp = ''
            c = 0
            correct = False
    
    answer = ''
    for i in range(len(loaf_c)-1, -1, -1):
        if loaf_c[i] == True:
            answer = loaf[i] + answer
        else:
            answer = '(' + answer + ')' + loaf[i][1:len(loaf[i])-1]
        
    return answer
  
  
  
  
  
# 2nd try (다른 사람의 풀이 참고)
# 재귀로 풀 수도 있구나 (머쓱)
def solution(p):
    # 아래 이거 없으면 can only concatenate str (not nonetype) to str 에러 난다 ('' 대신 None이 리턴되지 않게 조심!)
    if p == '': return p
    
    correct = False
    c = 0
    for i in range(len(p)):
        # 괄호 쌍 계산
        if p[i] == '(': c -= 1
        else: c += 1
        # 올바른 괄호 여부 확인
        if c < 0:
            correct = True
        # 쌍이 맞을 경우 재귀함수로 처리
        if c == 0:
            if correct:
                return p[:i+1] + solution(p[i+1:])
            else:
                return '(' + solution(p[i+1:]) + ')' + ''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i])))
