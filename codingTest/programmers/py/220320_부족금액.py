# https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3

def solution(price, money, count):
    answer = money - price * int(count*(count+1)/2)
    if answer < 0:
        return -1 * answer
    else: return 0
