#https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    s = s.replace("zero","0").replace("one","1").replace("two","2")
    .replace("three","3").replace("four","4").replace("five","5")
    .replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9")
    
    answer = int(s)
    return answer
  
  
  
#치환하거나 대응되는 일련의 뭉텅이가 있을 때, 배열이나 딕셔너리를 먼저 생각하자
#replace가 반복되니, 그것을 줄이는 방법을 고민했다면 생각했을 수도!

#string-num으로 이루어진 딕셔너리 생성
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key,value in num_dic.items():
        answer = answer.replace(key,value)
    return int(answer)
