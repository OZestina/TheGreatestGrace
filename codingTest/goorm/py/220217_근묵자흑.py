# https://level.goorm.io/exam/47881/%EA%B7%BC%EB%AC%B5%EC%9E%90%ED%9D%91/quiz/1

# 올림 사용을 위한 import
from math import ceil

[N, K] = [int(x) for x in input().split()]
input() #필요없는 input값 처리

print(ceil( (N-1) / (K-1) ))
