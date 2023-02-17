# https://school.programmers.co.kr/learn/courses/30/lessons/159993

# 1st try
def solution(maps):
    to_lever = 0
    to_exit = 0
    
    width = len(maps[0])
    height = len(maps)
    
    map_ori = [[-1] * width for _ in range(height)]
    map_lever = [[0] * width for _ in range(height)]
    map_exit = [[0] * width for _ in range(height)]
    pos = dict()
    
    #maps => map_ori
    for x in range(height):
        for y in range(width):
            if maps[x][y] != 'X':
                map_ori[x][y] = 1
                if maps[x][y] != 'O':
                    pos[maps[x][y]] = [x, y]
            else:
                map_ori[x][y] = 0
    #S => 'L'
    deck = [pos['S']]
    while deck:
        x, y = deck.pop(0)
        if x > 0 and map_ori[x-1][y] and map_lever[x-1][y] == 0:
            deck.append([x-1, y])
            map_lever[x-1][y] = map_lever[x][y] + 1
        if x < height - 1 and map_ori[x+1][y] and map_lever[x+1][y] == 0:
            deck.append([x+1, y])
            map_lever[x+1][y] = map_lever[x][y] + 1
        if y > 0 and map_ori[x][y-1] and map_lever[x][y-1] == 0:
            deck.append([x, y-1])
            map_lever[x][y-1] = map_lever[x][y] + 1
        if y < width - 1 and map_ori[x][y+1] and map_lever[x][y+1] == 0:
            deck.append([x, y+1])
            map_lever[x][y+1] = map_lever[x][y] + 1
        if map_lever[pos['L'][0]][pos['L'][1]] > 0:
            to_lever = map_lever[pos['L'][0]][pos['L'][1]]
            break
    if not to_lever:
        return -1
    
    
    #'L' => 'E'
    deck = [pos['L']]
    while deck:
        x, y = deck.pop(0)
        if x > 0 and map_ori[x-1][y] and map_exit[x-1][y] == 0:
            deck.append([x-1, y])
            map_exit[x-1][y] = map_exit[x][y] + 1
        if x < height - 1 and map_ori[x+1][y] and map_exit[x+1][y] == 0:
            deck.append([x+1, y])
            map_exit[x+1][y] = map_exit[x][y] + 1
        if y > 0 and map_ori[x][y-1] and map_exit[x][y-1] == 0:
            deck.append([x, y-1])
            map_exit[x][y-1] = map_exit[x][y] + 1
        if y < width - 1 and map_ori[x][y+1] and map_exit[x][y+1] == 0:
            deck.append([x, y+1])
            map_exit[x][y+1] = map_exit[x][y] + 1
        if map_exit[pos['E'][0]][pos['E'][1]] > 0:
            to_exit = map_exit[pos['E'][0]][pos['E'][1]]
            break
    if not to_exit:
        return -1
    
    return to_lever + to_exit
