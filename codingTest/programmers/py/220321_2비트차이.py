# https://school.programmers.co.kr/learn/courses/30/lessons/77885


# 1st try
# (뒤에서부터) 0이 처음으로 나오는 자리를 계산해서 처리
# 맨 끝에 0이 처음 나오는 수는 모두 짝수였다..!
def solution(numbers):
    answer = []
    
    for number in numbers:
        t = bin(number)
        if t[len(t)-1] == '0':
            t = t[:len(t)-1] + "1"
        else:
            for i in range(len(t)-2, 1, -1):
                if t[i] == '0':
                    t = t[:i] + "10" + t[i+2:]
                    break
            else:
                t = t[:3] + "0" + t[3:]
        answer.append(int(t, 2))
    
    return answer

  
# 2nd try (다른 사람의 풀이 참고)
# 짝수인 경우 바로 +1 한 수를 append하도록 진행
# 홀수인 경우 [xor로 구한 값의 right shift 2 값에 1을 더한 값]이 가장 마지막 0 다음의 1이되는 수여서 더해주면 01 => 10 이 된다
def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            t = number + 1
        else:
            t = number + ((number ^ number+1) >> 2) + 1
        answer.append(t)
    
    return answer
