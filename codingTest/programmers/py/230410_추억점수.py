# 

# 1st try
# dictionary + try로 해결
def solution(name, yearning, photo):
    answer = []
    
    point = dict()
    for i in range(len(name)):
        point[name[i]] = yearning[i]
        
    for p in photo:
        temp = 0
        for ppl in p:
            try:
                temp += point[ppl]
            except:
                continue
        answer.append(temp)
    
    return answer
  

# 2nd try
# try 안해도 되네...
def solution(name, yearning, photo):
    point = dict()
    for i in range(len(name)):
        point[name[i]] = yearning[i]
    
    answer = []
    for pic in photo:
        temp = 0
        for p in pic:
            if p in point:
                temp += point[p]
        answer.append(temp)
    
    return answer
