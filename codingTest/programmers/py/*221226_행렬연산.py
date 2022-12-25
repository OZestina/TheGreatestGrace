# https://school.programmers.co.kr/learn/courses/30/lessons/118670

# 1st try => 효율성 실패
def rotate(rc, time, f, s, circle, arr):
    temp = [item[:] for item in rc]
    for i in range(circle):
        x, y = arr[(i + time) % circle]
        rc[x][y] = temp[arr[i][0]][arr[i][1]]

    
def shiftrow(rc, time, f, s):
    time = time % f
    if time > f // 2:
        for _ in range(f-time):
            rc.append(rc.pop(0))
            
    else:
        for _ in range(time):
            rc.insert(0, rc.pop())
    

def solution(rc, operations):
    f = len(rc)
    s = len(rc[0])
    circle = (f + s - 2) * 2
    arr = []
    for i in range(s): arr.append([0,i])
    for i in range(1, f-1): arr.append([i, s-1])
    for i in range(s): arr.append([f-1, s-i-1])
    for i in range(1, f-1): arr.append([f-i-1, 0])

    #operation은 묶어서 진행
    r, sr = 0, 0
    for i in operations:
        if i == "Rotate":
            if sr > 0:
                shiftrow(rc, sr, f, s)
                sr = 0
            r += 1
        else:
            if r > 0:
                rotate(rc, r, f, s, circle, arr)
                r = 0
            sr += 1
    #마지막 operation 진행
    if sr > 0:
        shiftrow(rc, sr, f, s)
    elif r > 0:
        rotate(rc, r, f, s, circle, arr)
        
    return rc
