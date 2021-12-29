# https://programmers.co.kr/learn/courses/30/lessons/64065

  
# 2nd try
# 모든 수의 개수를 세서 가장 많이 나온 수 부터 answer에 넣는 방법이 있었다.
# 1st try보다 더 시간/메모리 측면에서 더 낫다. 그리고 코드도 쉽다
# 다른 방법이 없을까 더 고민했으면 생각할 수 있었려나
def solution(s):
    s = s[2:len(s)-2].replace('},{',',').split(',')
    d = dict()
    for num in s:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    answer = [None] * len(d)
    for key in d:
        answer[len(d)-d[key]] = int(key)
    return answer

  
# 2nd) 다른 사람의 풀이
# 정규식으로 문자열 정돈 + Counter라는 새로운 방법으로 카운팅

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
  
# ==============================================================================

  
# 1st try
# 각 값을 set로 만들고 길이 순으로 정렬해서 각각의 차를 구하는 방법으로 풀긴했는데 뭔가 마음에 안든다
def solution(s):
    
    tuple_list = s.replace('{{','').replace('}}','').split("},{")
    tuples = [None]*len(tuple_list)
    
    for tup in tuple_list:
        tup = set(int(x) for x in tup.split(','))
        tuples[len(tup)-1] = tup
    
    for idx in range(len(tuples)-1, 0, -1):
        for num in tuples[idx] - tuples[idx-1]:
            tuples[idx] = num
            
    for num in tuples[0]:
            tuples[0] = num
            
    return tuples
  
# 길이 순으로 정렬하기
# key값을 len으로 주면 길이 순으로 정렬이 가능하다..!
    tuples.sort(key = len)

  
# 1st) 다른 사람의 풀이
# set가 아닌 not in 으로 해결, 시간/메모리는 1st 방법이 우위
def solution(s):
    answer = []
    
    tuple_list = s.replace('{{','').replace('}}','').split("},{")
    tuples = []
    
    for tup in tuple_list:
        tuples.append(tup.split(','))
        
    tuples.sort(key = len)
    
    for nums in tuples:
        for j in range(len(nums)):
            if int(nums[j]) not in answer:
                answer.append(int(nums[j]))
                break
    return answer
  
# 1st) 다른 사람의 풀이 2
# 읽기 쉽게 쓰여진 코드. 멋지다.
def solution(s):
    answer = []
    
    tuples = s[2:len(s)-2].split("},{")
    tuples.sort(key = len)
    
    for tup in tuples:
        tup = list(map(int, tup.split(',')))
        for num in tup:
            if num not in answer:
                answer.append(num)
                break
    return answer
