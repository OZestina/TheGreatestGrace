# https://programmers.co.kr/learn/courses/30/lessons/72412#

# 1st try => 실패, still thinking
def solution(info, query):
    answer = []

    new_info = [i.split() for i in info]
    new_query = [i.split() for i in query]

    for i in new_query:
        temp = [k for k in range(len(new_info))]

        if i[0] != '-':
            temp2 = []
            for k in range(len(temp)):
                if i[0][0] != new_info[temp[k]][0][0]:
                    temp2.append(temp[k])
            temp = [x for x in temp if x not in temp2]
        if i[2] != '-':
            temp2 = []
            for k in range(len(temp)):
                if i[2][0] != new_info[temp[k]][1][0]: temp2.append(temp[k])
            temp = [x for x in temp if x not in temp2]
        if i[4] != '-':
            temp2 = []
            for k in range(len(temp)):
                if i[4][0] != new_info[temp[k]][2][0]: temp2.append(temp[k])
            temp = [x for x in temp if x not in temp2]
        if i[6] != '-':
            temp2 = []
            for k in range(len(temp)):
                if i[6][0] != new_info[temp[k]][3][0]: temp2.append(temp[k])
            temp = [x for x in temp if x not in temp2]
        temp2 = []
        for k in range(len(temp)):
            if int(i[7]) > int(new_info[temp[k]][4]): temp2.append(temp[k])
        temp = [x for x in temp if x not in temp2]

        answer.append(len(temp))

    return answer
