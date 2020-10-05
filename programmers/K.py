def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        wtf = array[i-1:j]
        wtf.sort()
        answer.append(wtf[k-1])
    return answer