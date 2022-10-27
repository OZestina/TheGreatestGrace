# https://school.programmers.co.kr/learn/courses/30/lessons/131127

# 1st try
# discount에서 찾은 내용을 want의 인덱스 or -1(want에 없는 항목일 경우)로 바꿔두고 계산을 적게 하는 방식으로 진행
def solution(want, number, discount):
    len_want = len(want)
    count = [0 for i in range(len_want)]
    for i in range(10):
        for j in range(len_want):
            if discount[i] == want[j]:
                count[j] += 1
                discount[i] = j
                break
        else:
            discount[i] = -1
    
    answer = 1 if count == number else 0
    
    for i in range(10, len(discount)):
        if discount[i - 10] != -1:
            count[discount[i - 10]] -= 1
        for j in range(len_want):
            if discount[i] == want[j]:
                count[j] += 1
                discount[i] = j
                break
        else:
            discount[i] = -1
        if count == number: answer += 1
    
    return answer
  
  
  
# 다른 사람의 풀이
# Counter()의 리턴값(<class 'collections.Counter'>)과 dictionary는 비교할 수 있다 (상속관계였던듯)
# 이렇게 하면 시간제약에 걸릴 줄 알았는데 아니었다고 한다
from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer
