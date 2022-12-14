# https://school.programmers.co.kr/learn/courses/30/lessons/12904

# 1st try
def check_palindrome(s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l - i - 1]:
            return 0
    return l

def solution(s):
    answer = 1
    l = len(s)
    for i in range(l):
        for j in range(i+1, l):
            if j - i + 1 < answer:
                continue
            result = check_palindrome(s[i:j+1])
            if result > answer:
                answer = result
                
    return answer
