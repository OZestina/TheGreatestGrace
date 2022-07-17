#https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

#1st try
#함수 다 잊어버려서 다시 다 찾아서 했다^^
#중간에 ''.join(i), ' '.join(words) 로 써서 왜 계속 안되는지 몰랐던 것 반성...ㅠㅠ
# --> 그래도 안물어보고 스스로 깨우쳤으니 그나마 낫다고 위안을 합니다! (긍정긍정)
def solution(s):
    new_words = []
    words = s.split(' ')
    for i in words:
        word = []
        i.split()
        for j in range(len(i)):
            if j%2 == 0 :
                word.append(i[j].upper())
            else:
                word.append(i[j].lower())
        new_words.append(''.join(word))
    answer = ' '.join(new_words)
    return answer
  
#2nd try
#line 9의 words가 불필요한 변수여서 생략
#line 11의 word를 리스트 -> string 으로 수정 (리스트로 만들어서 합치는 연산과정 제거)
# 1) line 15, 17에서 append 대신 + 로 수정
# 2) line 18에서 ''.join(word)를 안해줘도 된다

def solution(s):
    words = []
    for i in s.split(' '):
        word = ''
        for j in range(len(i)):
            if j%2 == 0 :
                word = word + i[j].upper()
            else:
                word = word + i[j].lower()
        words.append(word)
    answer = ' '.join(words)
    return answer
  
#3rd
#저번에 배운 enumerate를 활용한 풀이. 인덱싱이 없어져서 좀 더 나은 것 같기도 하고,,?
def solution(s):
    words = []
    for i in s.split(' '):
        word = ''
        for j,v in enumerate(i):
            if j%2 == 0 :
                word += v.upper()
            else:
                word += v.lower()
        words.append(word)
    answer = ' '.join(words)
    return answer
  
#4th
#map과 lambda를 이용해 한 문장으로 표현한 방법이 있어요 (다른 사람 코드)
# map(함수, 리스트) / lambda 인자 : 표현식
#if i % 2 부분 너무 머싯써... 1 (True)이랑 0(False)만 나오는 거여서 가능한 것인듯!
def solution(s):
  return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
