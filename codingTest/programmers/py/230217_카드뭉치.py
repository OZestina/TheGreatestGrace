# https://school.programmers.co.kr/learn/courses/30/lessons/159994

# 1st try
def solution(cards1, cards2, goal):
    i_1, i_2 = 0, 0
    l_1, l_2 = len(cards1), len(cards2)
    for i in range(len(goal)):
        if i_1 < l_1 and goal[i] == cards1[i_1]:
            i_1 += 1
        elif i_2 < l_2 and goal[i] == cards2[i_2]:
            i_2 += 1
        else:
            return "No"
    
    return "Yes"
