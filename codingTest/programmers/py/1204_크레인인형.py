# https://programmers.co.kr/learn/courses/30/lessons/64061

#1st try
def solution(board, moves):
    size = len(board)
    count = 0         #터진 인형들 카운트 변수
    dollpos = []      #인형이 있는 각 좌표 저장 배열 생성
    for i in range(size):
        for j in range(size):
            if board[j][i] != 0:
                dollpos.append(j)
                break
    dolls = [0]       #크레인이 가져온 인형 저장 & 터지는 인형은 바로바로 터트리자
    for move in moves:
        if dollpos[move-1] > size-1:
            continue
        doll = board[dollpos[move-1]][move-1]
        dollpos[move-1] += 1
        if len(dolls) != 0 and dolls[len(dolls)-1] == doll:
            dolls.pop()
            count += 2
        else:
            dolls.append(doll)
    return count
  
#2nd try
def solution(board, moves):
    size = len(board)
    count = 0           #터진 인형들 카운트 변수
    dollpos = []        #인형이 있는 각 좌표 저장 배열 생성
    for i in range(size):
        for j in range(size):
            if board[j][i] != 0:
                dollpos.append(j)
                break
    dolls = [0]       #크레인이 가져온 인형 저장, 초기값으로 (의미없는 수인) 0을 넣어주면 line 19의 if문을 제외할 수 있다
    for move in moves:
        if dollpos[move-1] > size-1:
            continue
        doll = board[dollpos[move-1]][move-1]
        dollpos[move-1] += 1
        if dolls[len(dolls)-1] == doll:
            dolls.pop()
            count += 2
        else:
            dolls.append(doll)
    return count
  
# 다른 사람의 풀이
# 주어진 배열을 변형해 검색 코드를 간단히 만들었다
# zip(*board) 코드 너무 멋있다..! 각 열끼리 새로운 행이 되도록 만드는 코드!
def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])
    return a
