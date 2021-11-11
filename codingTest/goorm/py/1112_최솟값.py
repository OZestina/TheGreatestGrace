#https://level.goorm.io/exam/43125/%EC%B5%9C%EC%86%8C%EA%B0%92/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

length = int(input())
arr = list(map(int, input().split(" ")))

# 1)정렬 후 0번째 값 프린트
arr.sort()
print(arr[0])

# 2)배열의 최솟값 구하는 함수 사용
print(min(arr))
