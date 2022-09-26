# https://school.programmers.co.kr/learn/courses/30/lessons/42747#

# 1st try
# 이분탐색으로 연산 횟수 줄임
def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    start = 0
    end = len(citations) - 1
    while start <= end:
        check = (start + end) // 2
        if check + 1 <= citations[check]:
            answer = check + 1
            start = check + 1
        else:
            end = check - 1
    
    return answer

  
# 2nd try (다른 사람의 풀이)
# 코드가 더 직관적이다
# len() - idx 값이 남은 리스트의 개수인거로 하면 계산이 더 줄어든다..!

def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
