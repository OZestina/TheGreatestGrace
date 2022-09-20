#Q1: 괄호 ===================================================
# https://programmers.co.kr/skill_checks/419994?challenge_id=1468



#Q2: 자동완성 ================================================
# https://programmers.co.kr/skill_checks/419994?challenge_id=2440

def strstr(word, word2):
    l1 = len(word)
    l2 = len(word2)
    wlen = l1 if l1 <= l2 else l2
    count = 0
    while count < wlen:
        if word[count] == word2[count]:
            count += 1
        else:
            break
    if count == l1:
        return count
    return count+1

  
def overlap(words, i):
    if i == 0:
        return strstr(words[i], words[i+1])
    elif i == len(words) - 1:
        return strstr(words[i], words[i-1])
    else:
        t1 = strstr(words[i], words[i-1])
        t2 = strstr(words[i], words[i+1])
        return max(t1, t2)
    

def solution(words):
    answer = 0
    words.sort()
    
    for i in range(len(words)):
        answer += overlap(words, i)
        
    return answer
