# https://school.programmers.co.kr/learn/courses/30/lessons/138477#

# 1st try
def bin_arr(arr, s, k):
    if len(arr) == 0: arr.append(s)
    elif arr[-1] >= s:
        if len(arr) < k: arr.append(s)
    elif arr[0] <= s: arr.insert(0, s)
    else:
        start, end = 0, len(arr) - 1
        while start <= end:
            check = (start + end) // 2
            if arr[check] > s: start = check + 1
            elif arr[check] < s: end = check - 1
            else: break
        if arr[check] > s: arr.insert(check + 1, s)
        else: arr.insert(check, s)
    if len(arr) > k:
        arr.pop()
            

def solution(k, score):
    answer = []
    rank = []
    for s in score:
        bin_arr(rank, s, k)
        answer.append(rank[-1])
    
    return answer
  
  
  
# 2nd try (다른 사람의 풀이)
# 그냥 min()을 활용해도 되는 거였다
def solution(k, score):
    rank = []
    answer = []
    for s in score:
        rank.append(s)
        if len(rank) > k:
            rank.remove(min(rank))
        answer.append(min(rank))
    return answer
