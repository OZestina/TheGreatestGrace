# https://programmers.co.kr/learn/courses/30/lessons/84512

# 1st try => 성공
# 각 자리에 알파벳이 들어오는 순서에 따라 계산되도독 진행
# 마음에는 드는데, 0~4 계산하는데 단순 계산 실수로 오래걸려서 스스로에게 흥뿡이었다
def solution(word):
    dictionary = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5, 0:781, 1:156, 2:31, 3:6, 4:1}
    answer = 0
    for i in range(len(word)):
        answer += (dictionary[word[i]]-1) * dictionary[i] + 1
    return answer
  
  
# 2nd try: 다른 사람 풀이 참고
# 이게 내가 하고 싶었던 (근데 공식 구하려고 생각을 안해본ㅎㅎ) 풀이었다!
def solution(word):
    dictionary = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    answer = 0
    for i in range(len(word)):
        # 배수(0~4) * 자리수 + 1
        answer += dictionary[word[i]] * (5**(5-i) -1)/4 + 1
        # answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer
  
  
  
# 3rd try: 다른 사람의 풀이
# 3900개 정도밖에 안되니 모두 만들어서 sort하고 인덱스로 구하자
# 이중 for문을 한 줄로 쓸 수 있구나!
from itertools import product
solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1

# for i in range(5):
#     for c in product("AEIOU", repeat=i+1):
#         answer.append(''.join(c))
