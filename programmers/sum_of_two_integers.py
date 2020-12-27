#두 정수 사이의 합
def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    else:
        if a > b:
            c = b
            b = a
            a = c
        while b+1-a > 0:
            answer = answer + a
            a = a+1

    return answer
