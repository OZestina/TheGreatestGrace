#https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def question():
  line 12~13에서 answer = arr.remove(min(arr)) 라고 하면 왜 안되죠ㅠ
  
  answer = 요정님 답변
  return answer

#1st try
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        answer = arr
    else:
        answer = [-1]
    
    return answer
  
#2nd try
