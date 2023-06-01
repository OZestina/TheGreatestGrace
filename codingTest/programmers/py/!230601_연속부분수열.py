# https://school.programmers.co.kr/learn/courses/30/lessons/178870#

# 내가 한 시도
# 1) 인덱스 모두 순회하면서 sum()으로 모두 구함 => 효율성 극악
# 2) 인덱스 마지막부터 순회하면서 sum()으로 구함 => (1)보다 10배가량 빠르지만 통과 못함

# 1st try (다른 사람의 풀이)
# 왼쪽, 오른쪽 포인터를 이용해 매번 sum()을 사용하지 않고 진행
def solution(sequence, k):
    length = len(sequence)
    right = 0
    temp_sum = sequence[0]
    answer = [0, length-1]

    for left in range(length):
        # l에서 시작해서 k랑 같거나 더 큰 수가 될 때까지 더하기
        while right + 1 < length and temp_sum < k:
            right += 1
            temp_sum += sequence[right]
        # 같을경우, 더 짧은 answer일 경우 업데이트
        if temp_sum == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
        # 다음 l 검사하기 전 현재 l값 빼줌
        temp_sum -= sequence[left]

    return answer
