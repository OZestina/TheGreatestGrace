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

# 2nd try (23.02.24)
# 함수를 호출할 때 슬라이싱을 안하고 인덱스를 보내면 어떨까 싶었는데, 효율성은 크게 차이 없었다
def check_palindrome(s, start, end):
    l = end - start
    for i in range(l // 2):
        if s[start + i] != s[end - 1 - i]:
            return 0
    return l

def solution(s):
    answer = 1
    l = len(s)
    for i in range(l):
        for j in range(i+1, l):
            if j - i + 1 < answer:
                continue
            result = check_palindrome(s, i, j+1)
            if result > answer:
                answer = result
                
    return answer


# 3rd try (다른 사람 풀이 참고)
# 길이가 긴 부분문자열부터 확인해서 바로 리턴
def solution(s):
    length = len(s)
    # 전체가 펠린드롬일 때
    if s == s[::-1]:
        return length
    # 부분문자열 길이가 긴 것부터 확인, 바로 리턴
    for l in range(length - 1, 1, -1):
        for i in range(length - l + 1): #부분문자열 start 지점
            a = s[i:i + l]
            if a == a[::-1]:
                return l
    return 1
