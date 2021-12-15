# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

#각 수마다 좌표(x,y)를 지정해서 2580의 경우 [x값의 차이+y값의 차이]로 거리를 구하면 어떨까
#예이 성공 >-<
def solution(numbers, hand):
    key_position = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,2)]
    answer = ''
    left = key_position[10]     #'*'의 경우
    right = key_position[11]    #'#'의 경우
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = key_position[number]
        elif number in [3,6,9]:
            answer += 'R'
            right = key_position[number]
        else:                   #2580의 경우
            distance_left = abs(left[0]-key_position[number][0])+abs(left[1]-key_position[number][1])
            distance_right = abs(right[0]-key_position[number][0])+abs(right[1]-key_position[number][1])
            if distance_left > distance_right:
                answer += 'R'
                right = key_position[number]
            elif distance_left < distance_right:
                answer += 'L'
                left = key_position[number]
            else:               #거리가 같을 때
                if hand == 'left':
                    answer += 'L'
                    left = key_position[number]
                else:
                    answer += 'R'
                    right = key_position[number]
    return answer
