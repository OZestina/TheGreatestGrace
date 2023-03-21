# https://school.programmers.co.kr/learn/courses/30/lessons/17683

# 1st try
def replace_sharp(m):
    return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    # #음 정리
    m = replace_sharp(m)
    
    answer = ['(None)', 0]
    
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        melody = replace_sharp(melody)
        length = len(melody)
        
        start_h, start_m = start.split(':')
        end_h, end_m = end.split(':')
        time = (int(end_h) - int(start_h)) * 60 + int(end_m) - int(start_m)
        
        #radio: 라디오에서 나온 곡
        radio = melody * (time // length) + melody[:time % length]
        if radio.count(m) and answer[1] < time:
            answer = [title, time]
        
    return answer[0]
