# https://level.goorm.io/exam/49109/jmos/quiz/1

# Timeout 뜰까봐 조마조마했는데 그냥 바로 됐다!
user_input = int(input())
array = [int(x) for x in input().split()]
result = [0] * user_input

for i in range(user_input):
	maxi = 0
	for j in range(i):
		if array[j] < array[i] and result[j] > maxi:
			maxi = result[j]
	result[i] += maxi+1	

print(user_input - max(result))
