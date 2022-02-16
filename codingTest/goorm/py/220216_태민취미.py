# https://level.goorm.io/exam/49094/%ED%83%9C%EB%AF%BC%EC%9D%B4%EC%9D%98-%EC%B7%A8%EB%AF%B8/quiz/1

# 1~N까지 세제곱을 더한 값도 규칙이 있는 줄은 몰랐네
# (참고: 궁금해서 찾아본 계산법) https://sseong40.tistory.com/9

N = int(input())
print((N*(N+1) // 2)**2 % 1000000007)
