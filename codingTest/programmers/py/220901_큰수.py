#https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 22.12.19 다시 try
# 3rd try => 조금 더 나아졌지만 시간초과로 실패
def next_num(answer, k, number):
    
    if len(number) - k == 1:
        return [answer + max(number), 0, ""]
    
    pos = number.index(max(number[:k+1]))
    answer += number[pos]
    number = number[pos+1:]
    k -= pos
    return [answer, k, number]
    
def solution(number, k):
    answer = ''
    
    while k > 0:
        answer, k, number = next_num(answer, k, number)
        
    return answer + number



# 4th try => 다른 사람 풀이 참고, 통과!
# stack으로 바꿔서 하는 걸 생각을 못했다. 초기 내용으로 주어지는 answer = ''에 너무 매몰되지 말자!
def solution(number, k):
    answer = []
    
    for n in number:
        while answer and n > answer[-1] and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)
    
    return ''.join(answer[:len(answer) - k])


# =================================================================

# 1st try => fail (time out)
# number를 자꾸 업데이트해서 느린가?
def solution(number, k):
    for i in range(k):
        length = len(number)
        if length < 3:
            return number[0] if number[0] > number[1] else number [1]
        for j in range(1, length):
            if number[j-1] < number[j]:
                number = number[:j-1] + number[j:]
                break
            if j == length - 1:
                number = number[:j]
    return number
  
  
# 2nd try => fail (time out)
# number 업데이트 대신 자리를 기억해서 하면 더 빠를까 했는데 1st보다 느리다..!
def solution(number, k):
    pos = [i for i in range(len(number))]
    for _ in range(k): 
        for p in range(1, len(pos)):
            if number[pos[p-1]] < number[pos[p]]:
                pos.pop(p-1)
                break
            elif p + 1 == len(pos):
                pos.pop(p)
    answer = ''
    for p in pos:
        answer += number[p]
    return answer

