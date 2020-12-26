#연습문제 [2016년] 

def solution(a, b):
    calendar = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["THU","FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    dates = 0
    if a == 1:
        dates = b
    else:
        i=0
        while i < a-1:
            dates = dates + calendar[i]
            i = i+1
        dates = dates + b
        
    answer = date[dates%7]
    return answer
