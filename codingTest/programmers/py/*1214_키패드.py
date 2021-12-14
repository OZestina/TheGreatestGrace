# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

#테스트케이스도 통과 못함ㅎ
#2580을 어떻게 처리할지... (특히 0)
# 좀 더 생각해보자
def solution(numbers, hand):
    answer = ''
    left = right = 0
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = number+2   #right과 보폭맞춰!
        elif number in [3,6,9]:
            answer += 'R'
            right = number
        else:
            if abs(number-left) == abs(number-right):
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
            elif abs(number-left) > abs(number-right):
                answer += 'R'
                right = number
            else:
                answer += 'L'
                left = number
        
    return answer


#각 수마다 좌표(x,y)를 지정해서 2580의 경우 [x값의 차이+y값의 차이]로 거리를 구하면 어떨까
