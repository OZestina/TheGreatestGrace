# https://level.goorm.io/exam/43263/%ED%8A%B9%EC%A0%95-%EA%B5%AC%EA%B0%84%EC%9D%98-%ED%95%A9/quiz/1


user_input = input()
array = [int(x) for x in input().split(" ")]
[start, end] = [int(x) for x in input().split(" ")]

partial = 0
for i in range(start-1, end):
	partial += array[i]
	
print(partial)

# hangnew꺼 프린트 줍줍
# line 8~12를 하기 한 줄로 대체 가능! 머시썽
print(sum(array[start - 1:end]))
