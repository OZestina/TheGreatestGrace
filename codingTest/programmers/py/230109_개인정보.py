# https://school.programmers.co.kr/learn/courses/30/lessons/150370

# 1st try
def solution(today, terms, privacies):
    answer = []
    
    #today 정리 => y, m, d
    arr = today.split('.')
    today_int = [int(arr[0]), int(arr[1]), int(arr[2])]
    
    #terms 정리
    term = dict()
    for t in terms:
        c, n = t.split()
        term[c] = int(n)
    
    for p in range(len(privacies)):
        date, code = privacies[p].split()
        arr = date.split('.')
        year_check = int(arr[1]) + term[code] - 1
        not_ok_since = [int(arr[0]) + year_check // 12, year_check % 12 + 1, int(arr[2])]
        if today_int == not_ok_since:
            answer += [p + 1]
        else:
            for i in range(3):
                if not_ok_since[i] > today_int[i]:
                    break
                elif not_ok_since[i] < today_int[i]:
                    answer += [p + 1]
                    break
        
    return answer
  
# 2nd try (다른 사람 풀이 참고)
# 날짜 수(days)를 계산해 총 일수를 비교하는 방법. 더 빠르당!
def solution(today, terms, privacies):
    answer = []
    
    #today 정리 => total days since 2000.01.01
    today_int = [int(i) for i in today.split('.')]
    to_dates = (today_int[0] - 2000) * 336 + (today_int[1] - 1) * 28 + today_int[2]
    
    #terms 정리
    term = dict()
    for t in terms:
        c, n = t.split()
        term[c] = int(n)
    
    for p in range(len(privacies)):
        exp, code = privacies[p].split()
        exp_int = [int(i) for i in exp.split('.')]
        to_exp = (exp_int[0] - 2000) * 336 + (exp_int[1] - 1) * 28 + exp_int[2] + term[code] * 28
        if to_exp <= to_dates:
            answer += [p + 1]
    
    return answer
