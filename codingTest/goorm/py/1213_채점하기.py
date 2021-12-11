# https://level.goorm.io/exam/43280/%EC%B1%84%EC%A0%90%ED%95%98%EA%B8%B0/quiz/1

def grades(grade_str):
	result = 0
	for grade in grade_str.split('x'):
		length = len(grade)
		result += length*(length+1)//2
	return result

user_input = input()
print(grades(user_input))
