# https://school.programmers.co.kr/learn/courses/30/lessons/42579#

# 1st try
def solution(genres, plays):
    
    #count[genre] = [total play, first, second]
    count = dict()
    
    for i in range(len(genres)):
        if genres[i] in count:
            if plays[i] > plays[count[genres[i]][1]]:
                count[genres[i]][2] = count[genres[i]][1]
                count[genres[i]][1] = i
            elif count[genres[i]][2] == -1 or plays[i] > plays[count[genres[i]][2]]:
                count[genres[i]][2] = i
            count[genres[i]][0] += plays[i]
        else:
            count[genres[i]] = [plays[i], i, -1]
            
    answer = []
    gen = sorted(count, key = lambda x: -count[x][0])
    for g in gen:
        answer.append(count[g][1])
        if count[g][2] != -1:
            answer.append(count[g][2])

    return answer
