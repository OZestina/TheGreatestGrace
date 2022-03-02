# https://programmers.co.kr/learn/courses/30/lessons/42746

#str정렬로 시도
#3,30,34의 경우 34330의 순서가 돼야 가장 큰 수를 만들 수 있는데, 이 정렬은 어떻게 한담? (지금은 33034 순)
def solution(numbers):
    num_str = [str(x) for x in numbers]
    num_str.sort()
    num_str.reverse()
    return "".join(num_str)


# 22.03.02 이어서 품
# 각 숫자를 세자리까지 반복시킨 수로 정렬하면 된다 (numbers의 원소는 0 이상 1,000 이하입니다-라는 제약이 있다)
def solution(numbers):
    answer = ''
    n_list = []
    
    for num in numbers:
        temp = (str(num)*3)[:4]
        l = len(str(num))
        n_list.append([temp, l])
    
    n_list.sort(reverse=True)
    for (n,l) in n_list:
        answer += n[:l]
        
    if answer[0] == '0':
        return '0'
    
    return answer


# 다른 사람들의 어썸한 풀이
def solution(numbers):
    numbers = list(map(str, numbers))   # 그렇다 map()을 쓰면 되는 거였다
    numbers.sort(key=lambda x: x*3, reverse=True)   #그렇다 sort할 때 key를 줄 수 있었다
    return str(int(''.join(numbers)))   # 그렇다 join()으로 모두 합칠 수 있었다. (int->str은 0만 있는 경우 '0' 리턴을 위한 것)
