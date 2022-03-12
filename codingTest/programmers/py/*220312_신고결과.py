# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3

# 3rd try => ing
# 가장 긴 것부터 검사해서 len(v) < k 인 경우 탈출하는 방법 시도중
def solution(id_list, report, k):
    reported = {ids:[] for ids in id_list}
    mail = {ids:0 for ids in id_list}
    answer = []
    
    for comment in set(report):
        [reporter, bad] = comment.split()
        reported[bad].append(reporter)
    
    print(list(reported.values())
    # for v in [reported.values()].sort(reverse=True):
    #     print(v)
        # if len(v) < k: break
        # for reporter in v:
        #     mail[reporter] += 1
          
    # for ids in id_list:
    #     answer.append(mail[ids])
          
    return answer

# ============================================================================
# 1st try => 성공
def solution(id_list, report, k):
    reported = {ids:set() for ids in id_list}
    mail = {ids:0 for ids in id_list}
    answer = []
    
    for comment in report:
        [reporter, bad] = comment.split()
        reported[bad].add(reporter)
    
    for v in reported.values():
        if len(v) >= k:
            for reporter in v:
                mail[reporter] += 1
    
    for ids in id_list:
        answer.append(mail[ids])
    
    return answer
  
  
# 2nd try (다른 사람의 풀이 참고)
# 중복 값을 set() 처리로 아예 없애고 받을 수도 있다
def solution(id_list, report, k):
    reported = {ids:[] for ids in id_list}
    mail = {ids:0 for ids in id_list}
    answer = []
    
    for comment in set(report):
        [reporter, bad] = comment.split()
        reported[bad].append(reporter)
    
    for v in reported.values():
        if len(v) >= k:
            for reporter in v:
                mail[reporter] += 1
    
    for ids in id_list:
        answer.append(mail[ids])
    
    return answer
