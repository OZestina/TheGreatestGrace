# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    one_to_nine = {1,2,3,4,5,6,7,8,9}
    missing_num = one_to_nine - set(numbers)
    answer = sum(missing_num)
    return answer
  

#다른사람의 풀이에서 본 멋진 코드..!
#와... 멋있다....

def solution(numbers):
    return 45 - sum(numbers)
