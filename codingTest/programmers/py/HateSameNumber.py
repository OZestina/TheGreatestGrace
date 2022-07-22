#같은 숫자는 싫어!

def solution(arr):
    answer = []
    for a in arr:
        if len(answer) < 1:
            answer.append(a)
        elif answer[len(answer)-1] != a:
            answer.append(a)
        
    return answer

#어썸한 코드를 짜서 으쓱으쓱 :^]

#코딩요정님의 feedback/advice: 마지막에 append된 값을 별도의 변수로 저장해서 변수 a와 비교하면 연산과정이 적어진다
#(기존) 1.len 구해서 2.answer의 마지막 값을 찾고 3.그 값을 변수 a와 비교
#(변경) 1.별도로 저장된 마지막 append 값을 2.변수 a와 비교 --> 다만 이 경우에는 별도의 메모리가 추가됨 (하기 내용에서 last_num에 해당하는 메모리)

def solution(arr):
    answer = []
    last_num = None
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
            last_num = a
        elif last_num != a:
            answer.append(a)
            last_num = a
        
    return answer

#프로그래밍 시간이 줄어들었다! (예이! :^])
#효율성 테스트 시간 거의 절반으로 줄어듦!
