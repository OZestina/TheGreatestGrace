#https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3

'요정님 line34에 질문있어욥

#1st try
#각 자리수를 10, 100으로 나눠야 하나...생각하다가 일단 string으로 변환하는 방법으로 진행
def solution(n):
    answer = 0
    a = str(n)
    for i in list(a):
        answer += int(i)

    return answer
  
#2nd try
#위의 line7~8에서 굳이 문자열 변환한 것을 리스트로 안만들어도 된다는 것을 알게됨ㅎㅎ
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
  
#3rd try
#따끈따끈하게 오늘 배운(C책) 재귀함수를 이용한 방법
def solution(n):
    if n < 10:
        return n
    else:
        return n%10 + solution(n//10)
    'return n%10 + solution(n//10)
#line 26~27에서 굳이 else: 안쓰고 바로 return 해도 됨! (어짜피 if에 걸리는 것들은 다 걸러지니까)

#3-1 try
#3번째 방법인데 재귀함수 없이 해보자 --> while 사용 (재귀 vs 단순반복문 중 뭐가 더 나은가요? - 효율성/메모리 사용 등...)
def solution(n):
    a = 0
    while n > 0:
        a += n%10
        n = n // 10
    return a
  

