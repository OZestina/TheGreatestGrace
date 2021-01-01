#같은 숫자는 싫어!

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) < 1:
            answer.append(a)
        elif answer[len(answer)-1] != a:
            answer.append(a)
        
    return answer
