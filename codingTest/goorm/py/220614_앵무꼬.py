# https://level.goorm.io/exam/49053/%EC%95%B5%EB%AC%B4%EC%83%88-%EA%BC%AC%EA%BC%AC/quiz/1

user_input = int(input())

for i in range(user_input):
	temp = input()
	result = ""
	for i in range(len(temp)):
		if temp[i] in "aeiouAEIOU":
			result += temp[i]
	if len(result) == 0:
		print("???")
	else:
		print(result)
