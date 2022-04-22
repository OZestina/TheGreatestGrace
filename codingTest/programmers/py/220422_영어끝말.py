# https://programmers.co.kr/learn/courses/30/lessons/12981

# 1st  => 성공!
# set만드는 방법 다시 봄ㅎㅎ, words[0]을 word에서 안빼서 에러났었당ㅎ
def solution(n, words):
    word = set(words) - set([words[0]])
    flag = True
    
    for i in range(1, len(words)):
        # 끝말잇기 불일치
        if words[i - 1][len(words[i - 1]) - 1] != words[i][0]:
            flag = False
            break

        # 중복단어
        if words[i] in word:
            word = word - set([words[i]])
        else:
            flag = False
            break

    if flag == True:
        return [0, 0]
    else:  # [번호, 차례]
        return [i % n + 1, i // n + 1]
      
      
# 2nd try : 다른 사람의 풀이 참고
# 1) 아 맞다 [-1]! 리스트 마지막 원소는 -1로 접근이 가능했지^^;;
# 2) 굳이 set를 안만들고 그 전까지의 리스트 words[:i]에 있는 지만 확인하면 됐다!
def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [i % n + 1, i // n + 1]
    return [0, 0]
