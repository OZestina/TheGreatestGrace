#https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3

#1st try
#코딩하면서 자꾸 TypeError: 'int' object is not iterable 가 나오는데, 숫자 자료형은 반복문의 원소 그룹으로 사용할 수 없기에 나오는 메시지라고 합니다...ㅠ
#--> 이거 for i in '숫자' 로 써서 그런거였는데, for i in range(숫자) 로 하면 간단히 해결되는 문제였던것,,,,

#index out of list range 에러도 떴는데, 인덱스랑 len()이랑의 차이가 있어서 len()-1로 변경! 
#--> 위의 내용 중 for i in range(숫자)로 하면 더 편함

def solution(numbers):
    answer = []
    i = 0
    while i < len(numbers)-1:
        j = i+1
        while j <= len(numbers)-1:
            a = numbers[i]+numbers[j]
            if a not in answer:
                answer.append(a)
            j = j+1
        i = i+1
    
    answer.sort()
    
    return answer
    
#2nd try
#잊혀졌던 range와 set으로 다시 짜보자!
#set(집합 자료형)의 특징: 1) 중복이 없다 2) 순서가 없다(unordered, 그래서 인덱싱 불가)
# 인덱싱을 위해서는 list/tuple로 변환을 해야 하고, 이건 list(set_name) / tuple(set_name) 으로 가능하다!
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            else:
                answer.append(numbers[i]+numbers[j])
    
    a = sorted(list(set(answer)))
    
    return a
  
#3rd try
#range의 최소값을 설정할 수 있어서^^; line33에서 i+1로 해둘 경우 line34~36 없이 진행 가능!
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    a = sorted(list(set(answer)))
    
    return a
