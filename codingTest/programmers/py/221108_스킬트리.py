# https://school.programmers.co.kr/learn/courses/30/lessons/49993

# 1st try
def learn(skill, tree):
    i = 0
    for s in tree:
        if s == skill[i]:
            if i < len(skill) - 1: i += 1
        elif s in skill: return 0
    return 1

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        answer += learn(skill, tree)
    return answer
