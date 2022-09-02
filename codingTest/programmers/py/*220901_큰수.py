#https://school.programmers.co.kr/learn/courses/30/lessons/42883

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
