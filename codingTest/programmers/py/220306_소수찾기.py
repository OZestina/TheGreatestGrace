# https://programmers.co.kr/learn/courses/30/lessons/12921

# 1st try
# 소수만으로 나누는 것까지는 생각 => 실패 (효율성 테스트 실패)
# 추가로 제곱근 값보다 큰 p는 패스하는 것으로 변경 => 성공
def solution(n):
    # n은 2 이상이니 소수 2를 포함하는 것으로 시작
    # 2보다 큰 짝수는 모두 pass하는 것으로 한다
    answer = 1
    prime = [2]
    
    for i in range(3, n+1, 2):
        # print(prime)
        for p in prime:
            if i % p == 0: break
            elif p > i**(1/2): 
                answer += 1
                prime.append(i)
                break
    return answer

# 2nd try
# 소수 값 저장 외에 그냥 풀어도 되긴 됨
def solution(n):
    answer = 1
    for i in range(3, n+1, 2):
        for j in range(2, int(i ** (1/2)) + 1):
            if i % j == 0: break
        else: answer += 1
    return answer

  
# 3rd try (다른 사람의 풀이)
# set()를 이용해 배수를 모두 빼주는 코딩. 확실히 빠르다! 
def solution(n):
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)
