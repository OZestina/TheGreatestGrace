# https://school.programmers.co.kr/learn/courses/30/lessons/160586

# 1st try
def solution(keymap, targets):
    #알파벳별로 가장 빠른 키 개수 구하기
    alphabet = dict()
    for k in keymap:
        for i in range(len(k)):
            if k[i] not in alphabet:
                alphabet[k[i]] = i + 1
            else:
                if i < alphabet[k[i]]:
                    alphabet[k[i]] = i + 1
    #target마다의 키 수 구하기
    answer = []
    for target in targets:
        count = 0
        for t in target:
            try:
                count += alphabet[t]
            except:
                answer.append(-1)
                break
        else:
            answer.append(count)
    return answer
  
